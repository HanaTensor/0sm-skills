import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const VelocityPlot = () => {
  const data = [
    {radius: 1e-26, electron: 0.036950, muon: null},
    {radius: 1e-25, electron: 0.040134, muon: null},
    {radius: 3.428383905e-25, electron: 0.040374, muon: 0},
    {radius: 1e-24, electron: 0.040438, muon: 0.032907},
    {radius: 1e-23, electron: 0.040469, muon: 0.039881},
    {radius: 1e-22, electron: 0.040472, muon: 0.040512},
    {radius: 1e-21, electron: 0.040472, muon: 0.040574},
    {radius: 1e-19, electron: 0.040472, muon: 0.040581}
  ].filter(point => point.radius <= 1e-19);

  const formatRadius = (value) => {
    return `${value.toExponential(0)}`;
  };

  const formatVelocity = (value) => {
    if (value === 0) return "0";
    if (value === 0.045) return "0.045";
    if (value === 0.030) return "0.030";
    if (value === 0.015) return "0.015";
    return value?.toFixed(6);
  };

  return (
    <Card className="w-full">
      <CardContent className="pt-4">
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart 
              data={data}
              margin={{
                top: 20,
                right: 30,
                left: 20,
                bottom: 20
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="radius"
                type="number"
                scale="log"
                domain={[1e-26, 1e-19]}
                tickFormatter={formatRadius}
                label={{ value: 'Radius (m)', position: 'insideBottom', offset: -10, style: { fontSize: 21 } }}
                tick={{ fontSize: 21 }}
                ticks={[1e-26, 1e-25, 3e-25, 1e-24, 1e-23, 1e-22, 1e-21, 1e-19]}
              />
              <YAxis
                domain={[0, 0.045]}
                tickFormatter={formatVelocity}
                label={{ value: 'v/c', angle: -90, position: 'insideLeft', offset: 16, style: { fontSize: 21 } }}
                tick={{ fontSize: 21 }}
                ticks={[0, 0.015, 0.030, 0.045]}
              />
              <Tooltip
                formatter={(value, name) => [formatVelocity(value), name]}
                labelFormatter={(value) => `Radius: ${value.toExponential(2)} m`}
              />
              <Legend 
                verticalAlign="bottom" 
                height={36}
                wrapperStyle={{
                  bottom: 5,
                  paddingTop: 20
                }}
              />
              <Line
                type="monotone"
                dataKey="electron"
                stroke="#2196F3"
                name="Electron"
                dot={{ r: 4 }}
                strokeWidth={2}
                connectNulls={true}
              />
              <Line
                type="monotone"
                dataKey="muon"
                stroke="#F44336"
                name="Muon"
                dot={{ r: 4 }}
                strokeWidth={2}
                connectNulls={true}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  );
};

export default VelocityPlot;