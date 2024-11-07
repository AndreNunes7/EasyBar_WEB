"use client"

import React, { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Download, Plus, Minus, Trash2 } from 'lucide-react';
import { useToast } from "@/hooks/use-toast"

export default function InventoryManager() {
  const { toast } = useToast();
  
  const [inventory, setInventory] = useState([
    { id: 1, produto: 'Chopp Pilsen', quantidade: 10, contagem: 10 },
    { id: 2, produto: 'Chopp IPA', quantidade: 20, contagem: 20 },
    { id: 3, produto: 'Chopp Stout', quantidade: 15, contagem: 15 },
    { id: 4, produto: 'Chopp Weiss', quantidade: 12, contagem: 12 },
  ]);

  const updateQuantity = async (produto: string, newQuantity: number) => {
    try {
      const response = await fetch(`/editar/${produto}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ quantidade: newQuantity.toString() }).toString(),
      });

      if (response.ok) {
        setInventory((prev) =>
          prev.map((item) =>
            item.produto === produto ? { ...item, quantidade: newQuantity } : item
          )
        );
        
        toast({
          title: "Estoque atualizado",
          description: `${produto} foi atualizado com sucesso.`,
        });
      } else {
        throw new Error('Falha na atualização');
      }
    } catch (error) {
      toast({
        variant: "destructive",
        title: "Erro",
        description: "Não foi possível atualizar o estoque.",
      });
    }
  };

  const handleIncrement = (produto: string) => {
    const item = inventory.find((item) => item.produto === produto);
    if (item) {
      updateQuantity(produto, item.quantidade + 1);
    }
  };

  const handleDecrement = (produto: string) => {
    const item = inventory.find((item) => item.produto === produto);
    if (item && item.quantidade > 0) {
      updateQuantity(produto, item.quantidade - 1);
    }
  };

  const handleDelete = (produto: string) => {
    setInventory((prev) => prev.filter((item) => item.produto !== produto));
    toast({
      title: "Item removido",
      description: `${produto} foi removido do estoque.`,
    });
  };

  const handleDownload = async () => {
    try {
      const response = await fetch('/download_estoque');
      if (response.ok) {
        toast({
          title: "Download iniciado",
          description: "O arquivo do estoque está sendo baixado.",
        });
      }
    } catch (error) {
      toast({
        variant: "destructive",
        title: "Erro no download",
        description: "Não foi possível baixar o arquivo do estoque.",
      });
    }
  };

  return (
    <div className="container mx-auto py-8 px-4">
      <Card className="bg-white shadow-lg">
        <CardHeader className="text-center border-b">
          <CardTitle className="text-2xl font-bold text-gray-800">
            Controle de Estoque
          </CardTitle>
          <p className="text-gray-600">"nome do estabelecimento"</p>
        </CardHeader>
        <CardContent className="p-6">
          <div className="rounded-lg border">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead className="w-[300px]">Produto</TableHead>
                  <TableHead className="text-center">Quantidade</TableHead>
                  <TableHead className="text-center">Contagem</TableHead>
                  <TableHead className="text-center">Ajustar</TableHead>
                  <TableHead className="text-center">Ações</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {inventory.map((item) => (
                  <TableRow key={item.id}>
                    <TableCell className="font-medium">{item.produto}</TableCell>
                    <TableCell className="text-center">{item.quantidade}</TableCell>
                    <TableCell className="text-center">{Math.floor(item.contagem)}</TableCell>
                    <TableCell>
                      <div className="flex items-center justify-center gap-2">
                        <Button
                          variant="outline"
                          size="icon"
                          onClick={() => handleDecrement(item.produto)}
                          className="h-8 w-8"
                        >
                          <Minus className="h-4 w-4" />
                        </Button>
                        <Button
                          variant="outline"
                          size="icon"
                          onClick={() => handleIncrement(item.produto)}
                          className="h-8 w-8"
                        >
                          <Plus className="h-4 w-4" />
                        </Button>
                      </div>
                    </TableCell>
                    <TableCell className="text-center">
                      <Button
                        variant="destructive"
                        size="icon"
                        onClick={() => handleDelete(item.produto)}
                        className="h-8 w-8"
                      >
                        <Trash2 className="h-4 w-4" />
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>

          <div className="mt-6 flex justify-end">
            <Button
              onClick={handleDownload}
              className="bg-green-600 hover:bg-green-700"
            >
              <Download className="mr-2 h-4 w-4" />
              Baixar Estoque
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}