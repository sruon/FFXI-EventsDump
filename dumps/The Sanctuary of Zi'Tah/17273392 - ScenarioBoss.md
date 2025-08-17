# 17273392 - ScenarioBoss

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | The Sanctuary of Zi'Tah (ID: 121) |
| Block Size       | 144 bytes                         |
| Total Events     | 4                                 |
| References Count | 9                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      2 |              2 |
| [202](#event-202)        | 0x0002       |     33 |              6 |
| [65535.1](#event-655351) | 0x0023       |     10 |              2 |
| [65535.2](#event-655352) | 0x002D       |     30 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x3A544     |      238916 |
|       3 | 0x446EC     |      280300 |
|       4 | 0x0804      |        2052 |
|       5 | 0x0080      |         128 |
|       6 | 0x0078      |         120 |
|       7 | 0x000A      |          10 |
|       8 | 0x0258      |         600 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 2 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00 00                                             ..              
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0001 [0x00] END_REQSTACK()
```

### Event 202

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 33 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       92 01 30 92 07 01  22 00 2F 00 F8 FF FF 7F    ..0..."./.....
0010: 6C F8 FF FF 7F 00 80 01  80 37 02 80 03 80 00 80  l........7......
0020: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0002 [0x92] ScenarioBoss (ID: 17273392/0x01079230)->Render.Flags3 ^= 0x01
  1: 0x0008 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x000A [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  3: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  4: 0x0019 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=238.916*, z=280.300*, y=0.000*, direction=180.3°*
  5: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          6C F8 FF FF 7F  05 80 06 80 00              l.........   
```

#### Opcodes

```
  0: 0x0023 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=120*)
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 30 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         62 07 80               b..
0030: F8 FF FF 7F F8 FF FF 7F  6D 61 69 6E 00 80 1C 08  ........main....
0040: 80 6C F8 FF FF 7F 00 80  01 80 00                 .l.........     
```

#### Opcodes

```
  0: 0x002D [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[10*, 0*]
  1: 0x003E [0x1C] WAIT(600* ticks)
  2: 0x0041 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x004A [0x00] END_REQSTACK()
```
