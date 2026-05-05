import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const HamiltonianPlot = () => {
  const generateData = () => {
    const data = [];
    for (let i = 0; i <= 200; i++) {
      const phi = (i * 2 * Math.PI) / 200;
      data.push({
        phi: phi,
        cos4: Math.pow(Math.cos(phi/2), 4),
        sin4: Math.pow(Math.sin(phi/2), 4),
        sin2: 0.5 * Math.pow(Math.sin(phi), 2),
        H: Math.pow(Math.cos(phi/2), 4) + Math.pow(Math.sin(phi/2), 4) + 0.5 * Math.pow(Math.sin(phi), 2)
      });
    }
    return data;
  };

  const formatTick = (value) => {
    const pi = Math.PI;
    if (value === 0) return '0';
    if (value === pi/2) return 'π/2';
    if (value === pi) return 'π';
    if (value === 3*pi/2) return '3π/2';
    if (value === 2*pi) return '2π';
    return '';
  };

  return (
    <div className="w-full h-96 px-4 pt-4 pb-12">
      <ResponsiveContainer>
        <LineChart data={generateData()} margin={{ top: 20, right: 30, left: 20, bottom: 30 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis 
            dataKey="phi" 
            domain={[0, 2 * Math.PI]}
            ticks={[0, Math.PI/2, Math.PI, 3*Math.PI/2, 2*Math.PI]}
            tickFormatter={formatTick}
            label={{ value: 'Phase φ (= ωt)', position: 'bottom', offset: 10 }}
          />
          <YAxis 
            domain={[0, 1]}
            ticks={[0, 0.25, 0.50, 0.75, 1.00]}
            label={{ value: 'Value', angle: -90, position: 'insideLeft', offset: -10 }}
          />
          <Tooltip 
            formatter={(value) => value.toFixed(3)}
            labelFormatter={(label) => `φ = ${(label/(2*Math.PI)).toFixed(2)}π`}
          />
          <Legend 
            verticalAlign="top" 
            height={36}
            iconType="plainline"
          />
          <Line 
            type="monotone" 
            dataKey="cos4" 
            stroke="#1f77b4" 
            name="cos⁴(φ/2)"
            strokeDasharray="5 5"
            dot={false}
          />
          <Line 
            type="monotone" 
            dataKey="sin4" 
            stroke="#ff7f0e" 
            name="sin⁴(φ/2)"
            strokeDasharray="2 2"
            dot={false}
          />
          <Line 
            type="monotone" 
            dataKey="sin2" 
            stroke="#2ca02c" 
            name="(1/2)sin²(φ)"
            strokeDasharray="3 3"
            dot={false}
          />
          <Line 
            type="monotone" 
            dataKey="H" 
            stroke="#d62728" 
            name="H(φ)"
            strokeWidth={2}
            dot={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default HamiltonianPlot;