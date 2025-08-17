# 17142590 - Five Moons

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 200 bytes             |
| Total Events     | 5                     |
| References Count | 19                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [16](#event-16)          | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     31 |              7 |
| [65535.2](#event-655352) | 0x0027       |     15 |              5 |
| [65535.3](#event-655353) | 0x0036       |     34 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x3EE18     |      257560 |
|       2 | 0x7F086     |      520326 |
|       3 | 0x83C3      |       33731 |
|       4 | 0x001E      |          30 |
|       5 | 0x000A      |          10 |
|       6 | 0x3EE40     |      257600 |
|       7 | 0x7F1F6     |      520694 |
|       8 | 0x83DB      |       33755 |
|       9 | 0x0028      |          40 |
|      10 | 0x3EECB     |      257739 |
|      11 | 0x7FEB8     |      523960 |
|      12 | 0x848A      |       33930 |
|      13 | 0x3EEC0     |      257728 |
|      14 | 0x804FA     |      525562 |
|      15 | 0x84C9      |       33993 |
|      16 | 0x3F4FB     |      259323 |
|      17 | 0x818BA     |      530618 |
|      18 | 0x8460      |       33888 |

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

### Event 16

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
| Data Size    | 31 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 1E 42 93  05 01 4A 42 93 05 01 3E  ......B...JB...>
0020: 93 05 01 1C 04 80 00                              .......         
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=257.560*, Z=520.326*, Y=33.731*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x1E] EventEntity looks at Volker (ID: 17142594/0x01059342) and starts talking
  4: 0x001A [0x4A] Volker (ID: 17142594/0x01059342) looks at Five Moons (ID: 17142590/0x0105933E)
  5: 0x0023 [0x1C] WAIT(30* ticks)
  6: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  05 80 1F 00 06 80 07 80         2........
0030: 08 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=257.600*, Z=520.694*, Y=33.755*
  2: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   32 09  80 1F 00 0A 80 0B 80 0C        2.........
0040: 80 1F 01 1F 00 0D 80 0E  80 0F 80 1F 01 1F 00 10  ................
0050: 80 11 80 12 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x0036 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=257.739*, Z=523.960*, Y=33.930*
  2: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=257.728*, Z=525.562*, Y=33.993*
  4: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=259.323*, Z=530.618*, Y=33.888*
  6: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0057 [0x00] END_REQSTACK()
```
