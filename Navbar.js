import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-black text-white p-4 flex gap-6">
      <Link href="/">Consent</Link>
      <Link href="/dashboard">Dashboard</Link>
      <Link href="/logs">Logs</Link>
    </nav>
  );
}
