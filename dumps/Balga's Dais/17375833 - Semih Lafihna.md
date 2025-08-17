# 17375833 - Semih Lafihna

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Balga's Dais (ID: 146) |
| Block Size       | 100 bytes              |
| Total Events     | 4                      |
| References Count | 8                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [65535.2](#event-655352) | 0x001A       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x007F      |         127 |
|       1 | 0x0001      |           1 |
|       2 | 0x000A      |          10 |
|       3 | 0xFFFDE15D  |  4294828381 |
|       4 | 0xFFFCB1A0  |  4294750624 |
|       5 | 0xDA54      |       55892 |
|       6 | 0x0000      |           0 |
|       7 | 0x0096      |         150 |

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
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    6C F8 FF FF 7F 00 80  01 80 00                  l.........     
```

#### Opcodes

```
  0: 0x0001 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=127*, fade_time=1*)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 02 80 1F 00             2....
0010: 03 80 04 80 05 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-138.915*, Z=-216.672*, Y=55.892*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                6C F8 FF FF 7F 06            l.....
0020: 80 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=150*)
  1: 0x0023 [0x00] END_REQSTACK()
```
