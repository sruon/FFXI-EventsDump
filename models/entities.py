from dataclasses import dataclass, field


@dataclass
class Entity:

    entity_id: int
    name: str | None = None

    def get_display_name(self) -> str:
        prefix = self.name or "Unnamed NPC"
        return f"{prefix} (ID: {self.entity_id}/0x{self.entity_id:08X})"


@dataclass
class ZoneEntities:

    zone_id: int
    zone_name: str
    entities: list[Entity] = field(default_factory=list)
    _entity_map: dict[int, Entity] = field(default_factory=dict, init=False)

    def __post_init__(self):
        self._entity_map = {e.entity_id: e for e in self.entities}

    def get_entity_by_id(self, entity_id: int) -> Entity | None:
        return self._entity_map.get(entity_id)

    def get_entity_display_name(self, entity_id: int) -> str:
        entity = self.get_entity_by_id(entity_id)
        return entity.get_display_name() if entity else f"Unknown NPC (ID: {entity_id}/0x{entity_id:08X})"
