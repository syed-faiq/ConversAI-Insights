"use client";

import { useState, useEffect } from "react";
import { useMetrics } from "../../context/MetricsContext";
import { getProductivityAnalysis } from "../../services/productivityService";
import ProductivityReport from "../../components/ProductivityReport";

export default function ProductivityPage() {

  const { metrics } = useMetrics();
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

useEffect(() => {
  const fetchProductivity = async () => {
    if (!metrics) return;
    setLoading(true);
    try {
      const response = await getProductivityAnalysis(metrics);
      // Use productivity_analysis from API
      setReport(response.productivity_analysis);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  fetchProductivity();
}, [metrics]);

  if (!metrics) {
    return <p className="text-gray-500">Please upload chat data first on Dashboard.</p>;
  }

  return (
    <div className="space-y-6">
      {loading && <p className="text-gray-500">Running AI productivity analysis...</p>}
      {report && <ProductivityReport report={report} />}
    </div>
  );
}