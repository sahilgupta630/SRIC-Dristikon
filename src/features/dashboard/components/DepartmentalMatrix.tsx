import { motion, AnimatePresence } from 'motion/react';
import { Trophy, Lightbulb, TrendingUp, Medal, Crown, Star } from 'lucide-react';
import { useState } from 'react';

// --- REAL DATA FROM 2025 ANALYSIS ---
const leaderboards = {
    funding: [
        { rank: 1, name: "Mathematics & Directors Office", value: "251.1", count: 12, trend: "+15%" },
        { rank: 2, name: "SATHI Center (Infrastructure)", value: "240.6", count: 8, trend: "+8%" },
        { rank: 3, name: "Central Library", value: "125.3", count: 5, trend: "Stable" },
        { rank: 4, name: "Ocean Engg & Naval Arch", value: "123.9", count: 84, trend: "+12%" },
        { rank: 5, name: "Sponsored Research (SRIC)", value: "120.2", count: 156, trend: "+5%" },
    ],
    innovation: [
        { rank: 1, name: "Computer Science (CSE)", value: "24", count: 171, trend: "+45%" },
        { rank: 2, name: "Electronics & ECE", value: "18", count: 98, trend: "+30%" },
        { rank: 3, name: "Medical Science & Tech", value: "15", count: 64, trend: "+22%" },
        { rank: 4, name: "Chemistry Department", value: "13", count: 88, trend: "+10%" },
        { rank: 5, name: "G.S. Sanyal Telecom School", value: "12", count: 42, trend: "+18%" },
    ]
};

type TabType = 'funding' | 'innovation';

export function DepartmentalMatrix() {
    const [activeTab, setActiveTab] = useState<TabType>('funding');

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4, duration: 0.6 }}
            className="bg-gradient-to-br from-slate-800/90 to-slate-900/90 backdrop-blur-xl border border-white/10 rounded-2xl p-6 shadow-2xl h-full flex flex-col"
        >
            {/* HEADER */}
            <div className="flex items-center justify-between mb-6 shrink-0">
                <div className="flex items-center gap-4">
                    <div className={`p-3 rounded-2xl shadow-lg flex items-center justify-center transition-colors duration-500 ${activeTab === 'funding' ? 'bg-orange-500 shadow-orange-500/20' : 'bg-violet-500 shadow-violet-500/20'
                        }`}>
                        {activeTab === 'funding' ? (
                            <Trophy className="w-7 h-7 text-white stroke-[2.5]" />
                        ) : (
                            <Lightbulb className="w-7 h-7 text-white stroke-[2.5]" />
                        )}
                    </div>
                    <div>
                        <h3 className="text-white font-bold text-xl tracking-tight">Departmental Leaders</h3>
                        <p className="text-slate-400 text-sm font-medium">Top Performers of 2025</p>
                    </div>
                </div>
            </div>

            {/* TABS (Glassmorphism) */}
            <div className="flex p-1 bg-slate-800/60 rounded-xl border border-white/5 mb-6 shrink-0 relative">
                <div className="absolute inset-0 bg-white/5 rounded-xl pointer-events-none" />
                {(['funding', 'innovation'] as const).map((tab) => (
                    <button
                        key={tab}
                        onClick={() => setActiveTab(tab)}
                        className={`flex-1 py-2.5 rounded-lg text-sm font-bold flex items-center justify-center gap-2 transition-all duration-300 relative z-10 ${activeTab === tab
                            ? 'bg-white text-slate-900 shadow-md transform scale-[1.02]'
                            : 'text-slate-400 hover:text-white hover:bg-white/5'
                            }`}
                    >
                        {tab === 'funding' ? <TrendingUp size={20} /> : <Crown size={20} />}
                        <span className="capitalize">{tab} Powerhouse</span>
                    </button>
                ))}
            </div>

            {/* LIST */}
            <div className="flex-1 overflow-y-auto pr-1 min-h-0 custom-scrollbar flex flex-col">
                <AnimatePresence mode="wait">
                    <motion.div
                        key={activeTab}
                        initial={{ opacity: 0, x: 20 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, x: -20 }}
                        transition={{ duration: 0.3 }}
                        className="flex flex-col gap-3 h-full"
                    >
                        {leaderboards[activeTab].map((dept, index) => (
                            <motion.div
                                key={dept.name}
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: index * 0.1 }}
                                className="group relative bg-white/5 border border-white/20 rounded-xl p-4 hover:bg-white/10 hover:border-white/40 transition-all duration-300 shrink-0"
                            >
                                {/* Progress Bar Background */}
                                <div
                                    className={`absolute bottom-0 left-0 h-0.5 rounded-full transition-all duration-1000 ${activeTab === 'funding' ? 'bg-amber-500' : 'bg-violet-500'
                                        }`}
                                    style={{
                                        width: `${(1 - index * 0.15) * 100}%`,
                                        opacity: 0.6
                                    }}
                                />

                                <div className="flex items-center gap-4 relative z-10 w-full">
                                    {/* Rank Badge */}
                                    <div className="shrink-0 w-11 h-11 rounded-xl flex items-center justify-center font-black text-sm shadow-lg border border-white/10 bg-slate-800">
                                        {index <= 2 ? (
                                            <Crown
                                                size={18}
                                                className={
                                                    index === 0 ? "text-yellow-400 fill-yellow-400/20" :
                                                        index === 1 ? "text-slate-400 fill-slate-400/20" :
                                                            "text-white fill-white/20"
                                                }
                                            />
                                        ) : (
                                            <span className="text-slate-400">#{dept.rank}</span>
                                        )}
                                    </div>

                                    {/* Department Name & Count - Flex Grow to push Values to right */}
                                    <div className="flex-1 min-w-0 pr-2">
                                        <h4 className="text-white font-bold text-sm tracking-wide group-hover:text-blue-300 transition-colors truncate">
                                            {dept.name}
                                        </h4>
                                        <div className="flex items-center gap-2 text-xs text-slate-400 mt-1 font-medium">
                                            <Star size={12} className={index <= 2 ? "text-yellow-400 fill-yellow-400" : "text-slate-600"} />
                                            <span>{dept.count} Active Projects</span>
                                        </div>
                                    </div>

                                    {/* Value & Trend - Fixed alignment */}
                                    <div className="text-right shrink-0 flex flex-col items-end">
                                        <div className="font-bold text-lg text-white tracking-tight whitespace-nowrap">
                                            <span className="opacity-80 font-semibold mr-0.5">{activeTab === 'funding' ? '₹' : ''}</span>
                                            {dept.value}
                                            <span className="text-sm font-medium opacity-70 ml-1">{activeTab === 'funding' ? 'Cr' : 'Patents'}</span>
                                        </div>
                                        <div className="text-[11px] font-bold text-white mt-1 px-2 py-0.5 rounded-full bg-white/10 border border-white/5">
                                            {dept.trend}
                                        </div>
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                        {/* Spacer to Fill Height visually if list is short */}
                        <div className="flex-1" />
                    </motion.div>
                </AnimatePresence>
            </div>
        </motion.div>
    );
}