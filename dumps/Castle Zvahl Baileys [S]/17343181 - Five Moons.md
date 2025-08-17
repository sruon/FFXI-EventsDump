# 17343181 - Five Moons

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 224 bytes                          |
| Total Events     | 8                                  |
| References Count | 18                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [12](#event-12)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     15 |              5 |
| [65535.2](#event-655352) | 0x0017       |     20 |              6 |
| [65535.3](#event-655353) | 0x002B       |     16 |              4 |
| [65535.4](#event-655354) | 0x003B       |     14 |              4 |
| [65535.5](#event-655355) | 0x0049       |     16 |              4 |
| [65535.6](#event-655356) | 0x0059       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x56E7C     |      355964 |
|       2 | 0xFFFFAE8E  |  4294946446 |
|       3 | 0xFFFFD10D  |  4294955277 |
|       4 | 0x5058C     |      329100 |
|       5 | 0xFFFFAD78  |  4294946168 |
|       6 | 0xFFFFC162  |  4294951266 |
|       7 | 0x001E      |          30 |
|       8 | 0x0102      |         258 |
|       9 | 0x002D      |          45 |
|      10 | 0x4A3E4     |      304100 |
|      11 | 0x4A1A5     |      303525 |
|      12 | 0xFFFFBC01  |  4294949889 |
|      13 | 0xFFFFC176  |  4294951286 |
|      14 | 0x0028      |          40 |
|      15 | 0x492B3     |      299699 |
|      16 | 0x1009      |        4105 |
|      17 | 0xFFFFC17E  |  4294951294 |

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

### Event 12

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
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=355.964*, Z=-20.850*, Y=-12.019*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  00 80 1F 00 04 80 05 80         2........
0020: 06 80 1F 01 6F 1E D1 A2  08 01 00                 ....o......     
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=329.100*, Z=-21.128*, Y=-16.030*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0025 [0x1E] EventEntity looks at Allenberge (ID: 17343185/0x0108A2D1) and starts talking
  5: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   1C 07 80 6E CD             ...n.
0030: A2 08 01 08 80 99 CD A2  08 01 00                 ...........     
```

#### Opcodes

```
  0: 0x002B [0x1C] WAIT(30* ticks)
  1: 0x002E [0x6E] Five Moons (ID: 17343181/0x0108A2CD) uses emote 258*
  2: 0x0035 [0x99] Wait for Five Moons (ID: 17343181/0x0108A2CD) animation to complete
  3: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   1C 09 80 1F 00             .....
0040: 0A 80 05 80 06 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x003B [0x1C] WAIT(45* ticks)
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=304.100*, Z=-21.128*, Y=-16.030*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             1F 00 0B 80 0C 80 0D           .......
0050: 80 1F 01 1E D4 A2 08 01  00                       .........       
```

#### Opcodes

```
  0: 0x0049 [0x1F] MOVE_ENTITY: EventEntity moves to X=303.525*, Z=-17.407*, Y=-16.010*
  1: 0x0051 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0053 [0x1E] EventEntity looks at Flap (ID: 17343188/0x0108A2D4) and starts talking
  3: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             32 0E 80 1F 00 0F 80           2......
0060: 10 80 11 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0059 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=299.699*, Z=4.105*, Y=-16.002*
  2: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0066 [0x00] END_REQSTACK()
```
