"use client";

import { useMetrics } from "../context/MetricsContext";
import UploadForm from "../components/UploadForm";
import Dashboard from "./dashboard/page";

export default function Home() {

  const { metrics, setMetrics } = useMetrics();

  return (
    <div className="space-y-8">
      <UploadForm onUploadSuccess={setMetrics} />

      {metrics && <Dashboard metrics={metrics} />}
    </div>
  );
}