"use client"

import * as React from "react"
import { Bar, BarChart, CartesianGrid, XAxis } from "recharts"

import {
    Card,
    CardContent,
    CardDescription,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import {
    ChartConfig,
    ChartContainer,
    ChartLegend,
    ChartLegendContent,
    ChartTooltip,
    ChartTooltipContent,
} from "@/components/ui/chart"
import { ClassNames } from "@emotion/react"

export const description = "An interactive bar chart"

const chartData = [
    { month: "Janeiro", carne: 244, leite: 80 },
    { month: "Fevereiro", carne: 305, leite: 200 },
    { month: "Março", carne: 237, leite: 120 },
    { month: "Abril", carne: 73, leite: 190 },
    { month: "Maio", carne: 209, leite: 130 },
    { month: "Junho", carne: 214, leite: 140 },
    { month: "Julho", carne: 186, leite: 80 },
    { month: "Agosto", carne: 305, leite: 200 },
    { month: "Setembro", carne: 237, leite: 120 },
    { month: "Outubro", carne: 73, leite: 190 },
    { month: "Novembro", carne: 209, leite: 130 },
    { month: "Dezembro", carne: 214, leite: 140 },
]

const chartConfig = {
    views: {
        label: "Vendas p/ mês",
    },
    carne: {
        label: "Carne",
        color: "#082158",

    },
    leite: {
        label: "Leite",
        color: "#4b7ce6",
    },
} satisfies ChartConfig
export default function Despesas() {
    const [activeChart, setActiveChart] = React.useState<keyof typeof chartConfig>("carne")

    const total = React.useMemo(
        () => ({
            carne: chartData.reduce((acc, curr) => acc + curr.carne, 0),
            leite: chartData.reduce((acc, curr) => acc + curr.leite, 0),
        }),
        []
    )

    return (
        <Card>
            <CardHeader className="flex flex-col items-stretch space-y-0 border-b p-0 sm:flex-row">
                <div className="flex flex-1 flex-col justify-center gap-1 px-6 py-5 sm:py-6">
                    <CardTitle>Grafico de Despesas</CardTitle>
                    <CardDescription>
                        Despesas total nos ultimos 12 mesês
                    </CardDescription>
                </div>
                <div className="flex">
                    {["carne", "leite"].map((key) => {
                        const chart = key as keyof typeof chartConfig
                        return (
                            <button
                                key={chart}
                                data-active={activeChart === chart}
                                className="relative z-30 flex flex-1 flex-col justify-center gap-1 border-t px-6 py-4 text-left even:border-l data-[active=true]:bg-muted/50 sm:border-l sm:border-t-0 sm:px-8 sm:py-6"
                                onClick={() => setActiveChart(chart)}
                            >
                                <span className="text-xs text-muted-foreground">
                                    {chartConfig[chart].label}
                                </span>
                                <span className="text-lg font-bold leading-none sm:text-3xl">
                                    {total[key as keyof typeof total].toLocaleString()}
                                </span>
                            </button>
                        )
                    })}
                </div>
            </CardHeader>
            <CardContent className="px-2 sm:p-6">
                <ChartContainer config={chartConfig} className="aspect-auto h-[250px] w-full">
                    <BarChart accessibilityLayer data={chartData} margin={{ left: 12, right: 12, }}>
                        <CartesianGrid vertical={false} />
                        <XAxis
                            dataKey="month"
                            tickLine={false}
                            tickMargin={10}
                            axisLine={false}
                            tickFormatter={(value) => value.slice(0, 3)}
                        />
                        <ChartTooltip
                            content={
                                <ChartTooltipContent
                                    className="w-[150px]"
                                    nameKey="views"
                                />
                            }
                        />
                        <Bar dataKey={activeChart} fill={`var(--color-${activeChart})`} radius={4} />
                    </BarChart>
                </ChartContainer>
            </CardContent>
        </Card>
    )
}