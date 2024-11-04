"use client";
import { useState } from 'react';
import { Link } from 'react-router-dom';
import HomeIcon from '@mui/icons-material/Home';
import LogoutIcon from '@mui/icons-material/Logout';
import SettingsIcon from '@mui/icons-material/Settings';
import InsertChartIcon from '@mui/icons-material/InsertChart';
import RoomServiceIcon from '@mui/icons-material/RoomService';
import LocalShippingIcon from '@mui/icons-material/LocalShipping';
import PaidIcon from '@mui/icons-material/Paid';
import FilePresentIcon from '@mui/icons-material/FilePresent';
import LockIcon from '@mui/icons-material/Lock';

export function NavBar() {
    const [activeItem, setActiveItem] = useState('Menu');

    const menuItems = [
        { name: 'Menu', icon: <HomeIcon fontSize="medium" />, path: '/' },
        { name: 'DashBoard', icon: <InsertChartIcon fontSize="medium" />, path: '/dashboard' },
        { name: 'Cadastros', icon: <RoomServiceIcon fontSize="medium" />, path: '/cadastros' },
        { name: 'Estoque', icon: <LocalShippingIcon fontSize="medium" />, path: '/estoque' },
        { name: 'Financeiro', icon: <PaidIcon fontSize="medium" />, path: '/financeiro' },
        { name: 'Relatorios', icon: <FilePresentIcon fontSize="medium" />, path: '/relatorios' },
        { name: 'Configurações', icon: <SettingsIcon fontSize="medium" />, path: '/configuracoes' },
        { name: 'Segurança', icon: <LockIcon fontSize="medium" />, path: '/seguranca' },
        { name: 'Sair', icon: <LogoutIcon fontSize="medium" />, path: '/sair' },
    ];

    return (
        <nav className="bg-secundary flex flex-col text-sm items-center justify-between py-8">
            {menuItems.map((item) => (
                <Link to={item.path} key={item.name} onClick={() => setActiveItem(item.name)}>
                    <div
                        className={`text-background flex flex-col items-center cursor-pointer
                            ${activeItem === item.name ? 'text-background' : 'text-gray-500'}
                            hover:text-white transition-colors duration-300`}
                    >
                        {item.icon}
                        <p>{item.name}</p>
                    </div>
                </Link>
            ))}
        </nav>
    );
}
