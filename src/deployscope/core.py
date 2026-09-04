from collections.abc import Iterable, Mapping

def group(services: Iterable[Mapping[str,object]]) -> dict[str,list[str]]:
    """Group deployment service names by environment."""
    out={}
    for service in services:
        name=str(service.get('name','')).strip()
        env=str(service.get('environment','unknown')).strip() or 'unknown'
        if not name: raise ValueError('service name is required')
        out.setdefault(env,[]).append(name)
    return {k:sorted(v) for k,v in sorted(out.items())}
