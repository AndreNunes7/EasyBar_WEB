"use client"
import { useState } from 'react';
import HomeIcon from '@mui/icons-material/Home';
import LogoutIcon from '@mui/icons-material/Logout';
import SettingsIcon from '@mui/icons-material/Settings';
import InsertChartIcon from '@mui/icons-material/InsertChart';
import RoomServiceIcon from '@mui/icons-material/RoomService';

export function NavBar() {
    const [activeItem, setActiveItem] = useState('Menu');

    const menuItems = [
        { name: 'Menu', icon: <HomeIcon fontSize={'large'} /> },
        { name: 'Reserva', icon: <RoomServiceIcon fontSize={'large'} /> },
        { name: 'DashBoard', icon: <InsertChartIcon fontSize={'large'} /> },
        { name: 'Configuração', icon: <SettingsIcon fontSize={'large'} /> },
        { name: 'Sair', icon: <LogoutIcon fontSize={'large'} /> },
    ];

    return (
        <nav className="bg-secundary flex flex-col text-sm items-center justify-between py-8">
            {menuItems.map((item) => (
                <div
                    key={item.name}
                    className={`text-background flex flex-col items-center cursor-pointer
                        ${activeItem === item.name ? 'text-background' : 'text-gray-500'}
                        hover:text-white transition-colors duration-300`}
                    onClick={() => setActiveItem(item.name)}
                >
                    {item.icon}
                    <p>{item.name}</p>
                </div>
            ))}
        </nav>
    );
}
