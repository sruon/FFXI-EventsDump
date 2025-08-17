# 17343182 - Leki Shameene

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 204 bytes                          |
| Total Events     | 6                                  |
| References Count | 17                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [12](#event-12)          | 0x0001       |      7 |              2 |
| [13](#event-13)          | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     21 |              5 |
| [65535.2](#event-655352) | 0x0024       |     16 |              4 |
| [65535.3](#event-655353) | 0x0034       |     44 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0004      |           4 |
|       1 | 0x012C      |         300 |
|       2 | 0x001E      |          30 |
|       3 | 0x0008      |           8 |
|       4 | 0x0028      |          40 |
|       5 | 0x4A926     |      305446 |
|       6 | 0xFFFFB226  |  4294947366 |
|       7 | 0xFFFFC168  |  4294951272 |
|       8 | 0x49C6A     |      302186 |
|       9 | 0xFFFFB7E9  |  4294948841 |
|      10 | 0xFFFFC180  |  4294951296 |
|      11 | 0x49586     |      300422 |
|      12 | 0xFFFFC5DE  |  4294952414 |
|      13 | 0xFFFFC165  |  4294951269 |
|      14 | 0x492B3     |      299699 |
|      15 | 0x1009      |        4105 |
|      16 | 0xFFFFC17E  |  4294951294 |

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

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               6E                 n
0010: CE A2 08 01 00 80 99 CE  A2 08 01 1C 01 80 1E CA  ................
0020: A2 08 01 00                                       ....            
```

#### Opcodes

```
  0: 0x000F [0x6E] Leki Shameene (ID: 17343182/0x0108A2CE) uses emote 4*
  1: 0x0016 [0x99] Wait for Leki Shameene (ID: 17343182/0x0108A2CE) animation to complete
  2: 0x001B [0x1C] WAIT(300* ticks)
  3: 0x001E [0x1E] EventEntity looks at Volker (ID: 17343178/0x0108A2CA) and starts talking
  4: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1C 02 80 6E  CE A2 08 01 03 80 99 CE      ...n........
0030: A2 08 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0024 [0x1C] WAIT(30* ticks)
  1: 0x0027 [0x6E] Leki Shameene (ID: 17343182/0x0108A2CE) uses emote 8*
  2: 0x002E [0x99] Wait for Leki Shameene (ID: 17343182/0x0108A2CE) animation to complete
  3: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             32 04 80 1F  00 05 80 06 80 07 80 1F      2...........
0040: 01 1F 00 08 80 09 80 0A  80 1F 01 1F 00 0B 80 0C  ................
0050: 80 0D 80 1F 01 1F 00 0E  80 0F 80 10 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x0034 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=305.446*, Z=-19.930*, Y=-16.024*
  2: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=302.186*, Z=-18.455*, Y=-16.000*
  4: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=300.422*, Z=-14.882*, Y=-16.027*
  6: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=299.699*, Z=4.105*, Y=-16.002*
  8: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x005F [0x00] END_REQSTACK()
```
