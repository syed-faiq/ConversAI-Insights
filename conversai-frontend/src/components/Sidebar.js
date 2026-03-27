"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  BarChart3,
  ClipboardList,
} from "lucide-react";

export default function Sidebar() {
  const pathname = usePathname();

const menu = [
  { name: "Dashboard", path: "/", icon: LayoutDashboard },
  { name: "Productivity Report", path: "/productivity", icon: BarChart3 },
  { name: "Quiz", path: "/quiz", icon: ClipboardList },
  { name: "Evaluate Quiz", path: "/evaluate", icon: ClipboardList }, // new
];

  return (
    <aside className="w-64 bg-gradient-to-b from-gray-900 to-gray-800 text-white shadow-xl min-h-screen relative">
      
      {/* Logo */}
      <div className="p-6 border-b border-gray-700">
        <h1 className="text-2xl font-bold">ConversAI</h1>
        <p className="text-sm text-gray-400">Insights Dashboard</p>
      </div>

      {/* Menu */}
      <nav className="p-4 space-y-2">
        {menu.map((item, index) => {
          const Icon = item.icon;
          const isActive = pathname === item.path;

          return (
            <Link
              key={index}
              href={item.path}
              className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200
                ${
                  isActive
                    ? "bg-blue-600 text-white shadow-md"
                    : "text-gray-300 hover:bg-gray-700 hover:text-white"
                }`}
            >
              <Icon size={20} />
              <span>{item.name}</span>
            </Link>
          );
        })}
      </nav>

      {/* Footer */}
      <div className="absolute bottom-0 w-full p-4 border-t border-gray-700 text-sm text-gray-400">
        © 2026 ConversAI
      </div>
    </aside>
  );
}