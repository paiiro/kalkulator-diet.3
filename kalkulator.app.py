import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select";

export default function ProteinCalculator() {
  const [weight, setWeight] = useState(0);
  const [age, setAge] = useState(0);
  const [gender, setGender] = useState("");
  const [activity, setActivity] = useState("");
  const [goal, setGoal] = useState("");
  const [result, setResult] = useState(null);

  const calculateProtein = () => {
    let multiplier = 0;

    if (activity === "sedentary") multiplier = 0.8;
    else if (activity === "aktif") multiplier = 1.5;
    else if (activity === "atletik") multiplier = 2.0;

    if (goal === "cutting") multiplier += 0.2;
    else if (goal === "bulking") multiplier += 0.5;

    const proteinNeed = weight * multiplier;
    setResult(proteinNeed.toFixed(1));
  };

  return (
    <div className="max-w-xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4 text-center">Kalkulator Kebutuhan Protein Harian</h1>
      <Card className="shadow-md">
        <CardContent className="space-y-4 pt-6">
          <div>
            <Label>Berat Badan (kg)</Label>
            <Input type="number" onChange={(e) => setWeight(parseFloat(e.target.value))} />
          </div>
          <div>
            <Label>Umur</Label>
            <Input type="number" onChange={(e) => setAge(parseInt(e.target.value))} />
          </div>
          <div>
            <Label>Jenis Kelamin</Label>
            <Select onValueChange={setGender}>
              <SelectTrigger>
                <SelectValue placeholder="Pilih jenis kelamin" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="pria">Pria</SelectItem>
                <SelectItem value="wanita">Wanita</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <div>
            <Label>Tingkat Aktivitas</Label>
            <Select onValueChange={setActivity}>
              <SelectTrigger>
                <SelectValue placeholder="Pilih aktivitas" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="sedentary">Sedentary (jarang bergerak)</SelectItem>
                <SelectItem value="aktif">Aktif</SelectItem>
                <SelectItem value="atletik">Atletik</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <div>
            <Label>Tujuan</Label>
            <Select onValueChange={setGoal}>
              <SelectTrigger>
                <SelectValue placeholder="Pilih tujuan" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="maintenance">Menjaga Berat Badan</SelectItem>
                <SelectItem value="cutting">Menurunkan Berat Badan</SelectItem>
                <SelectItem value="bulking">Menaikkan Massa Otot</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <Button onClick={calculateProtein} className="w-full mt-4">
            Hitung Kebutuhan Protein
          </Button>

          {result && (
            <div className="text-center mt-6 text-lg font-semibold">
              Kebutuhan protein harian Anda: <span className="text-blue-600">{result} gram</span>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}