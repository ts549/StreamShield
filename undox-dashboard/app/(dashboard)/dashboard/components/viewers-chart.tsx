"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"

const data = [
  { name: "Mon", viewers: 2400 },
  { name: "Tue", viewers: 1398 },
  { name: "Wed", viewers: 9800 },
  { name: "Thu", viewers: 3908 },
  { name: "Fri", viewers: 4800 },
  { name: "Sat", viewers: 3800 },
  { name: "Sun", viewers: 4300 },
]

export function ViewersChart() {
  return (
    <Card className="bg-card border-border">
      <CardHeader>
        <CardTitle className="text-card-foreground">Weekly Incidents</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
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
            <Bar dataKey="viewers" fill="#15803d" radius={[4, 4, 0, 0]} />
          </BarChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  )
}
