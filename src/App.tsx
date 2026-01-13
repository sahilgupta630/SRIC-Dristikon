import { useState } from 'react';
import { motion } from 'motion/react';
import {
  DashboardHeader,
  KPIMetrics,
  ProjectImpactAnalytics,
  HighlightedFaculties,
  RecentProjects,
  DepartmentalMatrix,
  PatentAnalytics,
  CompanyCollaborations,
  DataRequirements
} from './features/dashboard';
import { ChatbotInterface } from './features/chatbot';
import { Database, MessageCircle } from 'lucide-react';

export default function App() {
  const [showDataRequirements, setShowDataRequirements] = useState(false);
  const [chatbotOpen, setChatbotOpen] = useState(false);

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900">
      {/* Animated Background Pattern */}
      <div className="fixed inset-0 opacity-10">
        <div className="absolute inset-0" style={{
          backgroundImage: 'radial-gradient(circle at 2px 2px, white 1px, transparent 0)',
          backgroundSize: '40px 40px'
        }} />
      </div>

      <div className="relative z-10">
        {/* Header */}
        <DashboardHeader />

        {/* Action Buttons */}
        <div className="container mx-auto px-4 py-4 flex gap-3">
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setShowDataRequirements(!showDataRequirements)}
            className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-purple-600 to-blue-600 text-white rounded-lg shadow-lg hover:shadow-xl transition-shadow"
          >
            <Database className="w-5 h-5" />
            {showDataRequirements ? 'Hide' : 'Show'} Data Requirements
          </motion.button>

          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => setChatbotOpen(!chatbotOpen)}
            className="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-green-600 to-emerald-600 text-white rounded-lg shadow-lg hover:shadow-xl transition-shadow"
          >
            <MessageCircle className="w-5 h-5" />
            {chatbotOpen ? 'Close' : 'Open'} AI Assistant
          </motion.button>
        </div>

        {/* Data Requirements Modal */}
        {showDataRequirements && <DataRequirements onClose={() => setShowDataRequirements(false)} />}

        <div className={`container mx-auto px-4 pb-12 transition-all duration-300 ${chatbotOpen ? 'mr-[400px]' : ''}`}>
          {/* KPI Overview */}
          <KPIMetrics />

          {/* Main Analytics Grid */}
          <div className="grid lg:grid-cols-3 gap-6 mb-6">
            <div className="lg:col-span-2 space-y-6">
              <ProjectImpactAnalytics />
            </div>
            <div>
              <DepartmentalMatrix />
            </div>
          </div>

          {/* Patent and Company Analytics */}
          <div className="grid lg:grid-cols-2 gap-6 mb-6">
            <PatentAnalytics />
            <CompanyCollaborations />
          </div>

          {/* Highlighted Faculties */}
          <HighlightedFaculties />

          {/* Recent Projects */}
          <RecentProjects />
        </div>
      </div>

      {/* Chatbot Side Panel */}
      <ChatbotInterface isOpen={chatbotOpen} onToggle={() => setChatbotOpen(!chatbotOpen)} />
    </div>
  );
}