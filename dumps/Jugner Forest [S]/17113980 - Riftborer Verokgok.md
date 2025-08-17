# 17113980 - Riftborer Verokgok

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Jugner Forest [S] (ID: 82) |
| Block Size       | 104 bytes                  |
| Total Events     | 4                          |
| References Count | 7                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [212](#event-212)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     12 |              4 |
| [65535.2](#event-655352) | 0x000E       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFA7285  |  4294603397 |
|       1 | 0xFFFB262C  |  4294649388 |
|       2 | 0xFFFFFFFA  |  4294967290 |
|       3 | 0xFFFA7142  |  4294603074 |
|       4 | 0xFFFB211B  |  4294648091 |
|       5 | 0x0000      |           0 |
|       6 | 0x000A      |          10 |

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

### Event 212

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1F 00 00 80 01 80  02 80 1F 01 6F 00          ..........o.  
```

#### Opcodes

```
  0: 0x0002 [0x1F] MOVE_ENTITY: EventEntity moves to X=-363.899*, Z=-317.908*, Y=-0.006*
  1: 0x000A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x000C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1F 00                ..
0010: 03 80 04 80 05 80 1F 01  6F 1C 06 80 4A 7C 23 05  ........o...J|#.
0020: 01 8F 23 05 01 6F 76 7C  23 05 01 00              ..#..ov|#...    
```

#### Opcodes

```
  0: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-364.222*, Z=-319.205*, Y=0.000*
  1: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0019 [0x1C] WAIT(10* ticks)
  4: 0x001C [0x4A] Riftborer Verokgok (ID: 17113980/0x0105237C) looks at Unnamed NPC (ID: 17113999/0x0105238F)
  5: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0026 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Riftborer Verokgok (ID: 17113980/0x0105237C) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x002B [0x00] END_REQSTACK()
```
