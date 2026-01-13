import { motion } from 'motion/react';
import { Rocket, CheckCircle2, Clock, AlertCircle } from 'lucide-react';

const deployments = [
  { id: 1, project: 'AI-Based Traffic Management', status: 'deployed', company: 'Smart City Corp', progress: 100, color: 'green' },
  { id: 2, project: 'IoT Energy Monitoring', status: 'testing', company: 'Green Energy Ltd', progress: 75, color: 'blue' },
  { id: 3, project: 'Blockchain Supply Chain', status: 'development', company: 'LogiTech Inc', progress: 45, color: 'yellow' },
  { id: 4, project: 'ML Predictive Maintenance', status: 'deployed', company: 'Manufacturing Pro', progress: 100, color: 'green' },
  { id: 5, project: 'Quantum Cryptography', status: 'testing', company: 'SecureNet', progress: 60, color: 'blue' },
  { id: 6, project: 'Robotics Automation', status: 'planning', company: 'AutoBot Systems', progress: 20, color: 'orange' }
];

const statusConfig = {
  deployed: { icon: CheckCircle2, label: 'Deployed', color: 'text-green-400', bg: 'bg-green-500/20', border: 'border-green-500/30' },
  testing: { icon: Clock, label: 'Testing', color: 'text-blue-400', bg: 'bg-blue-500/20', border: 'border-blue-500/30' },
  development: { icon: AlertCircle, label: 'Development', color: 'text-yellow-400', bg: 'bg-yellow-500/20', border: 'border-yellow-500/30' },
  planning: { icon: Clock, label: 'Planning', color: 'text-orange-400', bg: 'bg-orange-500/20', border: 'border-orange-500/30' }
};

export function DeploymentTracker() {
  return (
    <motion.div
      initial={{ opacity: 0, x: 20 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ delay: 0.4, duration: 0.6 }}
      className="bg-gradient-to-br from-slate-800/90 to-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl p-6 shadow-2xl h-full"
    >
      <div className="flex items-center gap-3 mb-6">
        <motion.div
          whileHover={{ rotate: 360 }}
          transition={{ duration: 0.6 }}
          className="p-2 bg-gradient-to-br from-cyan-500 to-blue-600 rounded-xl"
        >
          <Rocket className="w-6 h-6 text-white" />
        </motion.div>
        <div>
          <h3 className="text-white">Deployment Tracker</h3>
          <p className="text-slate-400 text-sm">Live project status</p>
        </div>
      </div>

      <div className="space-y-4 max-h-[500px] overflow-y-auto pr-2 custom-scrollbar">
        {deployments.map((deployment, index) => {
          const config = statusConfig[deployment.status as keyof typeof statusConfig];
          const StatusIcon = config.icon;

          return (
            <motion.div
              key={deployment.id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.5 + index * 0.1 }}
              whileHover={{ scale: 1.02, x: 5 }}
              className="bg-slate-700/30 border border-white/10 rounded-xl p-4 hover:border-white/20 transition-all"
            >
              <div className="flex items-start justify-between mb-3">
                <div className="flex-1">
                  <h4 className="text-white text-sm mb-1">{deployment.project}</h4>
                  <p className="text-slate-400 text-xs">{deployment.company}</p>
                </div>
                <div className={`flex items-center gap-1 px-2 py-1 ${config.bg} border ${config.border} rounded-lg`}>
                  <StatusIcon className={`w-3 h-3 ${config.color}`} />
                  <span className={`text-xs ${config.color}`}>{config.label}</span>
                </div>
              </div>

              {/* Progress Bar */}
              <div className="relative">
                <div className="h-2 bg-slate-800 rounded-full overflow-hidden">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${deployment.progress}%` }}
                    transition={{ delay: 0.6 + index * 0.1, duration: 1, ease: "easeOut" }}
                    className={`h-full bg-gradient-to-r ${deployment.color === 'green' ? 'from-green-500 to-emerald-500' :
                        deployment.color === 'blue' ? 'from-blue-500 to-cyan-500' :
                          deployment.color === 'yellow' ? 'from-yellow-500 to-amber-500' :
                            'from-orange-500 to-red-500'
                      } shadow-lg`}
                  />
                </div>
                <motion.span
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ delay: 0.8 + index * 0.1 }}
                  className="absolute -top-5 right-0 text-xs text-slate-300"
                >
                  {deployment.progress}%
                </motion.span>
              </div>
            </motion.div>
          );
        })}
      </div>

      <style>{`
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: rgba(51, 65, 85, 0.3);
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: rgba(99, 102, 241, 0.5);
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: rgba(99, 102, 241, 0.7);
        }
      `}</style>
    </motion.div>
  );
}
