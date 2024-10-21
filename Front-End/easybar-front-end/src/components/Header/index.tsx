import AccountCircleIcon from '@mui/icons-material/AccountCircle';

export function Header() {
    return (
        <header className="bg-secundary flex items-center justify-between pr-4 pl-12">
            <div className='text-background text-3xl'>
                EASYBAR
            </div>
            <div className='text-background text-sm flex flex-row items-center gap-2'>
                <div className='flex flex-col items-end'>
                    <p>Gabriel Alves Lopes</p>
                    <p>Gerente</p>
                </div>
                <AccountCircleIcon fontSize={'large'} />
            </div>
        </header>
    )
}