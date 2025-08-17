# 17064003 - Markovich

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Chocobo Circuit (ID: 70) |
| Block Size       | 208 bytes                |
| Total Events     | 8                        |
| References Count | 12                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [479](#event-479)        | 0x0001       |      1 |              1 |
| [488](#event-488)        | 0x0002       |      1 |              1 |
| [497](#event-497)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |      1 |              1 |
| [65535.2](#event-655352) | 0x0005       |     55 |              9 |
| [65535.3](#event-655353) | 0x003C       |     19 |              5 |
| [65535.4](#event-655354) | 0x004F       |     31 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x707EB     |      460779 |
|       2 | 0x5A0EF     |      368879 |
|       3 | 0x60FC      |       24828 |
|       4 | 0x001E      |          30 |
|       5 | 0x003C      |          60 |
|       6 | 0x70496     |      459926 |
|       7 | 0x5A72B     |      370475 |
|       8 | 0x5F97      |       24471 |
|       9 | 0x7242F     |      468015 |
|      10 | 0x65DF4     |      417268 |
|      11 | 0x5E10      |       24080 |

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

### Event 479

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

### Event 488

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 497

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             00                                        .           
```

#### Opcodes

```
  0: 0x0004 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0005   |
| Data Size    | 55 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                32 00 80  1F 00 01 80 02 80 03 80       2..........
0010: 1F 01 1E F0 FF FF 7F 1C  04 80 5B 05 80 43 60 04  ..........[..C`.
0020: 01 43 60 04 01 74 6C 6B  30 1C 05 80 5B 05 80 43  .C`..tlk0...[..C
0030: 60 04 01 43 60 04 01 74  6C 6B 31 00              `..C`..tlk1.    
```

#### Opcodes

```
  0: 0x0005 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0008 [0x1F] MOVE_ENTITY: EventEntity moves to X=460.779*, Z=368.879*, Y=24.828*
  2: 0x0010 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0012 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0017 [0x1C] WAIT(30* ticks)
  5: 0x001A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Markovich (ID: 17064003/0x01046043), Markovich (ID: 17064003/0x01046043)], work=60*
  6: 0x0029 [0x1C] WAIT(60* ticks)
  7: 0x002C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Markovich (ID: 17064003/0x01046043), Markovich (ID: 17064003/0x01046043)], work=60*
  8: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 00 80 1F              2...
0040: 00 06 80 07 80 08 80 1F  01 1E F0 FF FF 7F 00     ............... 
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=459.926*, Z=370.475*, Y=24.471*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 31 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               32                 2
0050: 00 80 1F 00 09 80 0A 80  0B 80 1F 01 1E F0 FF FF  ................
0060: 7F 1C 04 80 4A F0 FF FF  7F F8 FF FF 7F 00        ....J.........  
```

#### Opcodes

```
  0: 0x004F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=468.015*, Z=417.268*, Y=24.080*
  2: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0061 [0x1C] WAIT(30* ticks)
  5: 0x0064 [0x4A] LocalPlayer looks at EventEntity
  6: 0x006D [0x00] END_REQSTACK()
```
