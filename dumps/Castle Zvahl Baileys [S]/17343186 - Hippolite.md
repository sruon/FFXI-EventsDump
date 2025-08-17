# 17343186 - Hippolite

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Castle Zvahl Baileys [S] (ID: 138) |
| Block Size       | 232 bytes                          |
| Total Events     | 5                                  |
| References Count | 23                                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [12](#event-12)          | 0x0001       |      7 |              2 |
| [13](#event-13)          | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     44 |             10 |
| [65535.2](#event-655352) | 0x003B       |     44 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x49F21     |      302881 |
|       2 | 0xFFFFB9CD  |  4294949325 |
|       3 | 0xFFFFC180  |  4294951296 |
|       4 | 0x4A509     |      304393 |
|       5 | 0xFFFFB2AF  |  4294947503 |
|       6 | 0xFFFFC17D  |  4294951293 |
|       7 | 0x4AED2     |      306898 |
|       8 | 0xFFFFB1E0  |  4294947296 |
|       9 | 0xFFFFC14A  |  4294951242 |
|      10 | 0x4D654     |      317012 |
|      11 | 0xFFFFB152  |  4294947154 |
|      12 | 0x4A926     |      305446 |
|      13 | 0xFFFFB226  |  4294947366 |
|      14 | 0xFFFFC168  |  4294951272 |
|      15 | 0x49C6A     |      302186 |
|      16 | 0xFFFFB7E9  |  4294948841 |
|      17 | 0x49586     |      300422 |
|      18 | 0xFFFFC5DE  |  4294952414 |
|      19 | 0xFFFFC165  |  4294951269 |
|      20 | 0x492B3     |      299699 |
|      21 | 0x1009      |        4105 |
|      22 | 0xFFFFC17E  |  4294951294 |

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
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 1F 00 04 80  ................
0020: 05 80 06 80 1F 01 1F 00  07 80 08 80 09 80 1F 01  ................
0030: 1F 00 0A 80 0B 80 03 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=302.881*, Z=-17.971*, Y=-16.000*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=304.393*, Z=-19.793*, Y=-16.003*
  4: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=306.898*, Z=-20.000*, Y=-16.054*
  6: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=317.012*, Z=-20.142*, Y=-16.000*
  8: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 00 80 1F 00             2....
0040: 0C 80 0D 80 0E 80 1F 01  1F 00 0F 80 10 80 03 80  ................
0050: 1F 01 1F 00 11 80 12 80  13 80 1F 01 1F 00 14 80  ................
0060: 15 80 16 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=305.446*, Z=-19.930*, Y=-16.024*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=302.186*, Z=-18.455*, Y=-16.000*
  4: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=300.422*, Z=-14.882*, Y=-16.027*
  6: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=299.699*, Z=4.105*, Y=-16.002*
  8: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0066 [0x00] END_REQSTACK()
```
