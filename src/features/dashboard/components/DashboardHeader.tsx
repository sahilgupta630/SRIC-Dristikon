import { motion } from 'motion/react';
import { BarChart3, TrendingUp, Calendar } from 'lucide-react';

export function DashboardHeader() {
  const currentDate = new Date().toLocaleDateString('en-US', { 
    weekday: 'long', 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  });

  return (
    <motion.header
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="bg-gradient-to-r from-slate-800/80 to-blue-900/80 backdrop-blur-lg border-b border-white/10"
    >
      <div className="container mx-auto px-4 py-6">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div className="flex items-center gap-4">
            <motion.div
              initial={{ scale: 0, rotate: -180 }}
              animate={{ scale: 1, rotate: 0 }}
              transition={{ type: "spring", duration: 0.8 }}
              className="p-3 bg-gradient-to-br from-blue-500 to-purple-600 rounded-2xl shadow-lg"
            >
              <BarChart3 className="w-8 h-8 text-white" />
            </motion.div>
            <div>
              <motion.h1
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.2 }}
                className="text-white"
              >
                Drishtikon
              </motion.h1>
              <motion.p
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.3 }}
                className="text-blue-200"
              >
                IIT Kharagpur - Sponsored Research & Industrial Consultancy
              </motion.p>
            </div>
          </div>

          <div className="flex items-center gap-4">
            <motion.div
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.4 }}
              className="px-4 py-2 bg-white/10 backdrop-blur-sm rounded-lg border border-white/20"
            >
              <div className="flex items-center gap-2 text-blue-100">
                <Calendar className="w-4 h-4" />
                <span className="text-sm">{currentDate}</span>
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.5 }}
              className="px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-600 rounded-lg shadow-lg"
            >
              <div className="flex items-center gap-2 text-white">
                <TrendingUp className="w-4 h-4" />
                <span>Lead: Soumya</span>
              </div>
            </motion.div>
          </div>
        </div>
      </div>
    </motion.header>
  );
}
