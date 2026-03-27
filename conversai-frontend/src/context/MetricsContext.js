"use client";

import { createContext, useContext, useState } from "react";

const MetricsContext = createContext();

export function MetricsProvider({ children }) {
  const [metrics, setMetrics] = useState(null);

  return (
    <MetricsContext.Provider value={{ metrics, setMetrics }}>
      {children}
    </MetricsContext.Provider>
  );
}

export function useMetrics() {
  return useContext(MetricsContext);
}