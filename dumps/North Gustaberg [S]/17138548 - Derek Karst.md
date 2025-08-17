# 17138548 - Derek Karst

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 120 bytes                    |
| Total Events     | 7                            |
| References Count | 7                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [4](#event-4)            | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     22 |              6 |
| [65535.2](#event-655352) | 0x001E       |      4 |              2 |
| [65535.3](#event-655353) | 0x0022       |      4 |              2 |
| [65535.4](#event-655354) | 0x0026       |      2 |              2 |
| [13](#event-13)          | 0x0028       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0013      |          19 |
|       1 | 0x4955D     |      300381 |
|       2 | 0x7DBBE     |      515006 |
|       3 | 0xFFFF1618  |  4294907416 |
|       4 | 0x001E      |          30 |
|       5 | 0x0078      |         120 |
|       6 | 0x0000      |           0 |

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

### Event 4

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 1E 75 83  05 01 1C 04 80 00        ......u.......  
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 19* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=300.381*, Z=515.006*, Y=-59.880*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x1E] EventEntity looks at Pale Eagle (ID: 17138549/0x01058375) and starts talking
  4: 0x001A [0x1C] WAIT(30* ticks)
  5: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1C 05                ..
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x001E [0x1C] WAIT(120* ticks)
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       95 06 80 00                                   ....          
```

#### Opcodes

```
  0: 0x0022 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   96 00                                 ..        
```

#### Opcodes

```
  0: 0x0026 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x0027 [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0028  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0028 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002E [0x00] END_REQSTACK()
```
