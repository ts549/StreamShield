import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { TrendingUp, Users, Monitor, DollarSign, FileWarning, LucideMessageCircleWarning, MessageSquareWarning } from "lucide-react"

const metrics = [
  {
    title: "Total Streamers",
    value: "24,567",
    change: "+12.5%",
    icon: Users,
    trend: "up",
  },
  {
    title: "Active Streamers",
    value: "1,234",
    change: "+8.2%",
    icon: Monitor,
    trend: "up",
  },
  {
    title: "Number of Incidents",
    value: "5,600",
    change: "+15.3%",
    icon: MessageSquareWarning,
    trend: "up",
  },
  {
    title: "Incident Rate",
    value: "27.4%",
    change: "+3.1%",
    icon: TrendingUp,
    trend: "up",
  },
]

export function MetricsGrid() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {metrics.map((metric) => (
        <Card key={metric.title} className="bg-card border-border">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-card-foreground">{metric.title}</CardTitle>
            <metric.icon className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-card-foreground">{metric.value}</div>
            <p className="text-xs text-primary">{metric.change} from last month</p>
          </CardContent>
        </Card>
      ))}
    </div>
  )
}
