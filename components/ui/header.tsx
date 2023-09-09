import Link from 'next/link'
import MobileMenu from './mobile-menu'
import Image from 'next/image'
import TNova from '@/public/images/terr.png'

export default function Header() {
  return (
    <header className="absolute w-full z-30">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="flex items-center justify-between h-20 border-spacing-1">
          {/* Site branding */}
          
          <div className="flex-shrink-0 mr-4">
            {/* Logo */}
            <Link href="/" className="block" aria-label="Cruip">
              <Image src={TNova} width={250} height={250} alt="Cruip" />
            </Link>
          </div>

      
          

          {/* Desktop navigation */}
    
          <MobileMenu />

        </div>
      </div>
    </header>
  )
}
