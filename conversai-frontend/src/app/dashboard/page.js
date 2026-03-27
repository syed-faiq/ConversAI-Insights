"use client";

import { useState } from "react";
import MetricsCard from "../../components/MetricsCard";
import ChartCard from "../../components/ChartCard";
import { BarChart, Bar, XAxis, YAxis, Tooltip, PieChart, Pie, Cell, Legend, ResponsiveContainer } from "recharts";

export default function Dashboard({ metrics }) {
  const [data] = useState(metrics || {
    total_conversations: 20,
    total_messages: 150,
    user_messages: 100,
    assistant_messages: 50,
    avg_messages_per_conversation: 7.5,
    active_days: 10,
    messages_per_day: 15,
    dominant_topics: ["Python", "AI", "ML"],
    topic_metrics: {
      Python: { messages: 50, conversations: 10 },
      AI: { messages: 60, conversations: 5 },
      ML: { messages: 40, conversations: 5 }
    },
    learning_behavior: {
      primary_interest: "AI",
      secondary_interest: "Python",
      learning_intensity: "High",
      technical_usage: "Daily",
      learning_consistency: "Regular",
      engagement_depth: "Deep"
    }
  });

  const topicData = Object.entries(data.topic_metrics).map(([topic, info]) => ({
    topic,
    messages: info.messages
  }));

  const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#A569BD"];

  return (
    <div className="space-y-6">

      {/* Top Metrics */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
        <MetricsCard title="Total Conversations" value={data.total_conversations} small />
        <MetricsCard title="Total Messages" value={data.total_messages} small />
        <MetricsCard title="User Messages" value={data.user_messages} small />
        <MetricsCard title="Assistant Messages" value={data.assistant_messages} small />
      </div>

      {/* Average & Activity */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
        <MetricsCard title="Avg Msg / Conversation" value={data.avg_messages_per_conversation} small />
        <MetricsCard title="Active Days" value={data.active_days} small />
        <MetricsCard title="Messages / Day" value={data.messages_per_day} small />
      </div>

      {/* Learning Behavior */}
      <div>
        <h3 className="text-lg font-semibold mb-2 text-gray-700">Learning Behavior</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-3">
          <MetricsCard title="Primary Interest" value={data.learning_behavior.primary_interest} small />
          <MetricsCard title="Secondary Interest" value={data.learning_behavior.secondary_interest} small />
          <MetricsCard title="Learning Intensity" value={data.learning_behavior.learning_intensity} small />
          <MetricsCard title="Technical Usage" value={data.learning_behavior.technical_usage} small />
          <MetricsCard title="Learning Consistency" value={data.learning_behavior.learning_consistency} small />
          <MetricsCard title="Engagement Depth" value={data.learning_behavior.engagement_depth} small />
        </div>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <ChartCard title="Messages by Topic">
          <ResponsiveContainer width="100%" height={200}>
            <BarChart data={topicData}>
              <XAxis dataKey="topic" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="messages" fill="#4F46E5" />
            </BarChart>
          </ResponsiveContainer>
        </ChartCard>

        <ChartCard title="Topic Distribution">
          <ResponsiveContainer width="100%" height={200}>
            <PieChart>
              <Pie
                data={topicData}
                dataKey="messages"
                nameKey="topic"
                cx="50%"
                cy="50%"
                outerRadius={70}
                label
              >
                {topicData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </ChartCard>
      </div>

      {/* Dominant Topics */}
      <div>
        <h3 className="text-lg font-semibold mb-2 text-gray-700">Dominant Topics</h3>
        <div className="flex flex-wrap gap-2">
          {data.dominant_topics.map((topic, i) => (
            <span key={i} className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-xs">
              {topic}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}