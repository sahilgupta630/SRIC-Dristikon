import { motion } from 'motion/react';
import { FileText, Clock, DollarSign, Users, Sparkles, ChevronRight } from 'lucide-react';
import { useState } from 'react';

// --- REAL DATA: Projects Started Dec 2025 ---
// Source: No. of Projects started R.csv + C.csv
const projects = [
  {
    id: 1,
    title: 'Marine Toroidal Propellers: Hydrodynamics & Design',
    pi: 'Dr. Anirban Bhattacharyya',
    department: 'Ocean Engg',
    funding: 82,
    duration: '36 months',
    progress: 5, // Just Started (Dec 22, 2025)
    team: 7,
    summary: 'Investigation into toroidal propeller geometries to enhance propulsion efficiency and reduce underwater noise signature. Includes CFD modelling and hydrodynamic tank testing.',
    keywords: ['Hydrodynamics', 'Propulsion', 'Marine Tech'],
    status: 'In Progress'
  },
  {
    id: 2,
    title: 'Women\'s Health Tech: Community Adaptation',
    pi: 'Prof. Suman Chakraborty',
    department: 'Mech Engg',
    funding: 35,
    duration: '18 months',
    progress: 8,
    team: 12,
    summary: 'Deployment of low-cost, microfluidic-based diagnostic devices for women\'s health monitoring in rural communities. Focuses on technology adaptation for non-clinical settings.',
    keywords: ['Microfluidics', 'Public Health', 'Diagnostics'],
    status: 'In Progress'
  },
  {
    id: 3,
    title: 'Keystone Species DSS for High Altitude Wetlands',
    pi: 'Dr. Mukunda Dev Behera',
    department: 'CORAL',
    funding: 27,
    duration: '24 months',
    progress: 5,
    team: 6,
    summary: 'Developing a Decision Support System (DSS) using satellite telemetry and AI to manage carbon services and protect keystone species in Himalayan wetland ecosystems.',
    keywords: ['AI/ML', 'Remote Sensing', 'Ecology'],
    status: 'In Progress'
  },
  {
    id: 4,
    title: 'Shipyard Field Investigation & Numerical Modelling',
    pi: 'Prof. Ranadev Datta',
    department: 'Ocean Engg',
    funding: 76,
    duration: '2 months',
    progress: 15, // Short term consultancy
    team: 4,
    summary: 'Rapid field survey and numerical simulation for proposed shipyard infrastructure. Assesses soil stability and wave load impact for structural safety.',
    keywords: ['Simulation', 'Infrastructure', 'Survey'],
    status: 'In Progress'
  },
  {
    id: 5,
    title: 'Dual-Phase High Entropy Alloys (FeMnCrCo)',
    pi: 'Dr. Shibayan Roy',
    department: 'Materials',
    funding: 27,
    duration: '24 months',
    progress: 5,
    team: 5,
    summary: 'Development of heterogeneous microstructures in medium entropy alloys to overcome the strength-ductility trade-off. targets applications in high-stress industrial components.',
    keywords: ['Alloys', 'Metallurgy', 'Material Science'],
    status: 'In Progress'
  },
  {
    id: 6,
    title: 'Slope Stability Analysis: Soapstone Mine',
    pi: 'Dr. Abhiram Kumar Verma',
    department: 'Mining',
    funding: 11,
    duration: '8 months',
    progress: 10,
    team: 3,
    summary: 'Geotechnical assessment of dump and pit slope stability for the Bhungapat Soapstone Mine. Utilizes rock mechanics modelling to prevent landslides.',
    keywords: ['Mining', 'Safety', 'Geotech'],
    status: 'In Progress'
  }
];

export function RecentProjects() {
  const [expandedProject, setExpandedProject] = useState<number | null>(null);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.8, duration: 0.6 }}
    >
      <motion.h2
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ delay: 0.9 }}
        className="text-white mb-6 flex items-center gap-3 text-2xl font-bold"
      >
        <span className="w-1.5 h-8 bg-gradient-to-b from-blue-500 to-cyan-600 rounded-full" />
        New Project Arrivals
        <span className="text-sm text-slate-400 font-normal mt-1">(Dec 2025)</span>
      </motion.h2>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map((project, index) => (
          <motion.div
            key={project.id}
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 1 + index * 0.1, duration: 0.5 }}
            whileHover={{ scale: 1.02, y: -5 }}
            className="relative group cursor-pointer"
            onClick={() => setExpandedProject(expandedProject === project.id ? null : project.id)}
          >
            {/* Glow Effect */}
            <div className="absolute inset-0 bg-gradient-to-br from-blue-500/20 to-purple-500/20 opacity-0 group-hover:opacity-100 transition-opacity duration-500 rounded-2xl blur-xl" />

            <div className="relative bg-gradient-to-br from-slate-800/90 to-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl p-6 shadow-2xl hover:border-white/20 transition-all h-full flex flex-col">
              {/* Status Badge */}
              <div className="absolute top-4 right-4">
                <div className="px-2 py-0.5 rounded-full text-[8px] font-bold uppercase tracking-wider bg-blue-500/10 text-blue-300 border border-blue-500/20">
                  {project.status}
                </div>
              </div>

              {/* Title */}
              <h3 className="text-white font-bold text-lg leading-snug mb-3 pr-20 line-clamp-2 h-14">
                {project.title}
              </h3>

              {/* PI Info */}
              <div className="flex items-center gap-3 mb-6 border-b border-white/5 pb-6">
                <div className="w-10 h-10 bg-slate-800 rounded-full flex items-center justify-center text-white text-sm font-bold border border-white/10 shadow-inner">
                  {project.pi.split(' ')[1].charAt(0)}
                </div>
                <div>
                  <p className="text-white text-sm font-semibold truncate max-w-[180px]">{project.pi}</p>
                  <p className="text-white text-xs font-medium mt-1">{project.department}</p>
                </div>
              </div>

              {/* ML Summary Box */}
              <div className={`mb-4 p-3 bg-slate-900/50 border border-white/5 rounded-xl transition-all duration-500 ${expandedProject === project.id ? 'max-h-96' : 'max-h-24 overflow-hidden'
                }`}>
                <div className="flex items-center gap-2 mb-2">
                  <Sparkles className="w-3 h-3 text-purple-400" />
                  <p className="text-purple-300 text-xs font-bold uppercase tracking-wider">Project Scope</p>
                </div>
                <p className="text-white text-xs leading-relaxed">
                  {project.summary}
                </p>
              </div>

              {expandedProject !== project.id && (
                <div className="flex items-center gap-1 text-blue-400 text-xs mb-4 hover:underline">
                  <span>View Details</span>
                  <ChevronRight className="w-3 h-3" />
                </div>
              )}

              {/* Keywords */}
              <div className="flex flex-wrap gap-2 mb-5">
                {project.keywords.map((keyword) => (
                  <span
                    key={keyword}
                    className="px-2 py-1 bg-slate-800 text-white text-[10px] font-bold uppercase tracking-wide rounded-md border border-white/5"
                  >
                    {keyword}
                  </span>
                ))}
              </div>

              {/* Stats Grid */}
              <div className="grid grid-cols-3 gap-2 mt-auto">
                <div className="bg-slate-800/50 rounded-lg p-2 text-center border border-white/5">
                  <DollarSign className="w-3.5 h-3.5 text-green-400 mx-auto mb-1" />
                  <p className="text-white text-sm font-bold">₹{project.funding}L</p>
                  <p className="text-slate-300 text-[9px] uppercase font-bold">Value</p>
                </div>
                <div className="bg-slate-800/50 rounded-lg p-2 text-center border border-white/5">
                  <Clock className="w-3.5 h-3.5 text-blue-400 mx-auto mb-1" />
                  <p className="text-white text-sm font-bold">{project.duration.split(' ')[0]}</p>
                  <p className="text-slate-300 text-[9px] uppercase font-bold">Months</p>
                </div>
                <div className="bg-slate-800/50 rounded-lg p-2 text-center border border-white/5">
                  <Users className="w-3.5 h-3.5 text-purple-400 mx-auto mb-1" />
                  <p className="text-white text-sm font-bold">{project.team}</p>
                  <p className="text-slate-300 text-[9px] uppercase font-bold">Team</p>
                </div>
              </div>

              {/* Progress Bar */}
              <div className="mt-4 pt-3 border-t border-white/5">
                <div className="flex items-center justify-between mb-1.5">
                  <span className="text-slate-300 text-[10px] font-bold uppercase tracking-wider">Phase 1 Initiation</span>
                  <span className="text-blue-400 text-xs font-bold">{project.progress}%</span>
                </div>
                <div className="h-1.5 bg-slate-800 rounded-full overflow-hidden">
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${project.progress}%` }}
                    transition={{ delay: 1.2 + index * 0.1, duration: 1 }}
                    className="h-full bg-gradient-to-r from-blue-500 to-cyan-400"
                  />
                </div>
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </motion.div>
  );
}