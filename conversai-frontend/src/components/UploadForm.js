"use client";

import { useState } from "react";
import { UploadCloud, FileText, Info, ChevronDown, ChevronUp } from "lucide-react";
import Button from "./Button";
import { uploadChatFile } from "../services/uploadService";

export default function UploadForm({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [showGuide, setShowGuide] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    try {
      const data = await uploadChatFile(file);
      onUploadSuccess(data);
    } catch (err) {
      alert(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white border border-gray-200 shadow-sm rounded-xl p-4 max-w-md">

      {/* Header */}
      <div className="flex items-center justify-between mb-3">
        <h2 className="text-sm font-semibold text-gray-800">Upload Chat</h2>

        <button
          onClick={() => setShowGuide(!showGuide)}
          className="text-gray-400 hover:text-blue-500"
        >
          <Info size={16} />
        </button>
      </div>

      {/* Upload Row */}
      <div className="flex items-center gap-3">

        {/* Upload Box */}
        <label className="flex items-center gap-2 border border-dashed border-gray-300 rounded-lg px-3 py-2 cursor-pointer hover:border-blue-400 hover:bg-blue-50 transition flex-1">
          <UploadCloud className="w-5 h-5 text-blue-500" />
          <span className="text-xs text-gray-600 truncate">
            {file ? file.name : "Choose file"}
          </span>
          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
            className="hidden"
          />
        </label>

        {/* Upload Button */}
        <Button
          onClick={handleUpload}
          disabled={!file || loading}
          className="bg-blue-600 hover:bg-blue-700 text-white text-xs px-4 py-2 rounded-lg disabled:bg-gray-300"
        >
          {loading ? "..." : "Upload"}
        </Button>
      </div>

      {/* File Preview */}
      {file && (
        <div className="flex items-center gap-2 mt-2 text-xs text-gray-500">
          <FileText className="w-4 h-4" />
          <span className="truncate">{file.name}</span>
        </div>
      )}

      {/* Minimal Guide */}
      {showGuide && (
        <div className="mt-3 text-xs text-gray-600 bg-gray-50 border rounded-md p-3 space-y-2">
          <p>Export chat from ChatGPT/Gemini as .txt, .json, or .csv.</p>
          <p>You can also upload a .zip file received via email from chatgpt or gemini.</p>
        </div>
      )}
    </div>
  );
}