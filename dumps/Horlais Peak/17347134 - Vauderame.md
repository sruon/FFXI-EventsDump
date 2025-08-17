# 17347134 - Vauderame

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Horlais Peak (ID: 139) |
| Block Size       | 80 bytes               |
| Total Events     | 3                      |
| References Count | 4                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |     19 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x002D      |          45 |
|       3 | 0x0096      |         150 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    6C F8 FF FF 7F 00 80  01 80 92 01 F8 FF FF 7F   l..............
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x000A [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 19 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1C 02 80 6C F8 FF FF  7F 00 80 03 80 92 01 F8   ...l...........
0020: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0011 [0x1C] WAIT(45* ticks)
  1: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=150*)
  2: 0x001D [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x0023 [0x00] END_REQSTACK()
```
