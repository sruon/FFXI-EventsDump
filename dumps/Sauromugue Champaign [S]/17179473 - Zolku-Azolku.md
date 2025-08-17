# 17179473 - Zolku-Azolku

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 164 bytes                         |
| Total Events     | 7                                 |
| References Count | 9                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [9](#event-9)            | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     15 |              5 |
| [65535.2](#event-655352) | 0x0017       |     13 |              3 |
| [65535.3](#event-655353) | 0x0024       |     14 |              4 |
| [10](#event-10)          | 0x0032       |      7 |              2 |
| [65535.4](#event-655354) | 0x0039       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x00C9      |         201 |
|       2 | 0x13B82     |       80770 |
|       3 | 0xFFFFEC79  |  4294962297 |
|       4 | 0x0202      |         514 |
|       5 | 0x01BB      |         443 |
|       6 | 0x1291A     |       76058 |
|       7 | 0xFFFFFB64  |  4294966116 |
|       8 | 0x13A7A     |       80506 |

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

### Event 9

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
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=0.201*, Z=80.770*, Y=-4.999*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      6E  51 23 06 01 04 80 99 51         nQ#.....Q
0020: 23 06 01 00                                       #...            
```

#### Opcodes

```
  0: 0x0017 [0x6E] Zolku-Azolku (ID: 17179473/0x01062351) uses emote 514*
  1: 0x001E [0x99] Wait for Zolku-Azolku (ID: 17179473/0x01062351) animation to complete
  2: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 00 80 1F  00 05 80 06 80 03 80 1F      2...........
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.443*, Z=76.058*, Y=-4.999*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0032  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       92 01 F8 FF FF 7F  00                         .......       
```

#### Opcodes

```
  0: 0x0032 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 00 80 1F 00 07 80           2......
0040: 08 80 03 80 1F 01 1E 46  23 06 01 7B F8 FF FF 7F  .......F#..{....
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.180*, Z=80.506*, Y=-4.999*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x1E] EventEntity looks at Ragelise (ID: 17179462/0x01062346) and starts talking
  4: 0x004B [0x7B] EventEntity stops talking
  5: 0x0050 [0x00] END_REQSTACK()
```
