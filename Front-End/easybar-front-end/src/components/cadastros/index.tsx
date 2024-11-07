import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Checkbox, FormControlLabel, FormGroup } from '@mui/material';

const RegistrationForm = () => {
  const handleSubmit = (e: { preventDefault: () => void; }) => {
    e.preventDefault();
  };

  return (
    <div className="min-h-screen bg-gray-50 p-4 flex items-center justify-center">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle className="text-2xl font-bold text-gray-900">Cadastro</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <Input
                type="text"
                placeholder="Nome completo"
                className="w-full rounded-md"
                required
              />
            </div>
            <div>
              <Input
                type="text"
                placeholder="CPF"
                className="w-full rounded-md"
              />
            </div>
            <div>
              <Input
                type="number"
                placeholder="Telefone"
                className="w-full rounded-md"
                required
              />
            </div>
            <div>
              <Input
                type="text"
                placeholder="Cargo"
                className="w-full rounded-md"
                required
              />
            </div>
            
            <div>
              <select
                className="w-full rounded-md border-gray-300 text-gray-700"
                defaultValue=""
                required
              >
                <option value="" disabled>Papel</option>
                <option value="admin">Administrador</option>
                <option value="funcionario">Funcionário</option>
                <option value="gerente">Gerente</option>
              </select>
            </div>

            <Button
              type="submit"
              className="w-full bg-blue-600 hover:bg-blue-700 text-white"
            >
              Enviar Ficha
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default RegistrationForm;
