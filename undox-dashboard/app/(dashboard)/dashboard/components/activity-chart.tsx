"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"

const data = [
  { name: "00:00", viewers: 4000 },
  { name: "04:00", viewers: 3000 },
  { name: "08:00", viewers: 2000 },
  { name: "12:00", viewers: 2780 },
  { name: "16:00", viewers: 1890 },
  { name: "20:00", viewers: 2390 },
  { name: "24:00", viewers: 3490 },
]

export function ActivityChart() {
  return (
    <Card className="bg-card border-border">
      <CardHeader>
        <CardTitle className="text-card-foreground">Number of Incidents (24h)</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#6b7280" />
            <XAxis dataKey="name" stroke="#f1f5f9" />
            <YAxis stroke="#f1f5f9" />
            <Tooltip
              contentStyle={{
                backgroundColor: "#374151",
                border: "1px solid #6b7280",
                borderRadius: "8px",
                color: "#f1f5f9",
              }}
            />
            <Line
              type="monotone"
              dataKey="viewers"
              stroke="#15803d"
              strokeWidth={2}
              dot={{ fill: "#15803d", strokeWidth: 2, r: 4 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  )
}
