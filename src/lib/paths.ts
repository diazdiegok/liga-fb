export const base = import.meta.env.BASE_URL;

export function asset(path: string) {
  return `${base}${path.replace(/^\//, "")}`;
}

export function page(path: string) {
  const clean = path.replace(/^\//, "");
  return `${base}${clean}`;
}
