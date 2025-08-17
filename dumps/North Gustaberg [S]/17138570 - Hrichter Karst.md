# 17138570 - Hrichter Karst

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 132 bytes                    |
| Total Events     | 4                            |
| References Count | 10                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [13](#event-13)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     37 |              7 |
| [65535.2](#event-655352) | 0x002D       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x15A6A     |       88682 |
|       2 | 0x2505      |        9477 |
|       3 | 0xFFFFB136  |  4294947126 |
|       4 | 0x001E      |          30 |
|       5 | 0x0005      |           5 |
|       6 | 0x000D      |          13 |
|       7 | 0x16B41     |       92993 |
|       8 | 0x28C7      |       10439 |
|       9 | 0xFFFFB127  |  4294947111 |

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

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 37 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 1E 74 83  05 01 1C 04 80 66 05 80  ......t......f..
0020: 8A 83 05 01 8A 83 05 01  74 6C 62 30 00           ........tlb0.   
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=88.682*, Z=9.477*, Y=-20.170*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x1E] EventEntity looks at Derek Karst (ID: 17138548/0x01058374) and starts talking
  4: 0x001A [0x1C] WAIT(30* ticks)
  5: 0x001D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [Hrichter Karst (ID: 17138570/0x0105838A), Hrichter Karst (ID: 17138570/0x0105838A)], work=5*
  6: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 06 80               2..
0030: 1F 00 07 80 08 80 09 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=92.993*, Z=10.439*, Y=-20.185*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003B [0x00] END_REQSTACK()
```
