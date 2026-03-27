import json
import zipfile
import io
from router_utils import metrics_router_utils


async def handle_upload(file):
    filename = file.filename
    contents = await file.read()

    # JSON upload
    if filename.endswith(".json"):
        conversations = json.loads(contents)
        messages = extract_messages(conversations)
        metrices = metrics_router_utils.compute_metrics(messages, len(conversations))

        return {
            "message": "JSON processed successfully",
            "total_conversations": len(conversations),
            **metrices
        }

    # ZIP upload
    elif filename.endswith(".zip"):
        zip_buffer = io.BytesIO(contents)
        all_conversations = []

        with zipfile.ZipFile(zip_buffer, "r") as zip_ref:
            for name in zip_ref.namelist():
                if name.startswith("conversations") and name.endswith(".json"):
                    with zip_ref.open(name) as f:
                        data = json.load(f)
                        all_conversations.extend(data)

        messages = extract_messages(all_conversations)
        metrices = metrics_router_utils.compute_metrics(messages, len(all_conversations))

        return {
            "message": "ZIP processed successfully",
            "total_conversations": len(all_conversations),
            **metrices
        }

    # TXT upload
    elif filename.endswith(".txt"):
        lines = contents.decode("utf-8").splitlines()
        messages = []

        for i, line in enumerate(lines, start=1):
            if not line.strip():
                continue
            messages.append({
                "role": "user",  # assuming all txt lines are user messages
                "text": line.strip(),
                "time": None,
                "conversation_id": f"txt_{i}"
            })

        metrices = metrics_router_utils.compute_metrics(messages, len(messages))

        return {
            "message": "TXT processed successfully",
            "total_messages": len(messages),
            **metrices
        }

    else:
        return {"error": "Unsupported file type. Upload JSON, ZIP, or TXT file."}


def extract_messages(conversations):
    messages = []
    for convo in conversations:
        convo_id = convo.get("id")
        mapping = convo.get("mapping", {})

        for node in mapping.values():
            message = node.get("message")
            if not message:
                continue

            role = message.get("author", {}).get("role")
            parts = message.get("content", {}).get("parts", [])
            text = parts[0] if parts else ""
            time = message.get("create_time")

            messages.append({
                "role": role,
                "text": text,
                "time": time,
                "conversation_id": convo_id
            })
    return messages