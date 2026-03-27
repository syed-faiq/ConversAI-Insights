import "./globals.css";
import { MetricsProvider } from "../context/MetricsContext";
import Sidebar from "../components/Sidebar";

export const metadata = {
  title: "ConversAI Insights",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="bg-gray-100">
        <MetricsProvider>

          {/* Sidebar */}
          <div className="fixed top-0 left-0 h-screen w-64">
            <Sidebar />
          </div>

          {/* Main Content */}
          <main className="ml-64 p-6">
            {children}
          </main>

        </MetricsProvider>
      </body>
    </html>
  );
}