# 17776848 - ChehRaihah

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 108 bytes             |
| Total Events     | 6                     |
| References Count | 7                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10151](#event-10151)    | 0x0001       |      1 |              1 |
| [10209](#event-10209)    | 0x0002       |      1 |              1 |
| [10211](#event-10211)    | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     22 |              6 |
| [65535.2](#event-655352) | 0x001A       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF28BD  |  4294912189 |
|       2 | 0x19718     |      104216 |
|       3 | 0x0000      |           0 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFE8830  |  4294871088 |
|       6 | 0x29AE1     |      170721 |

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

### Event 10151

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

### Event 10209

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

### Event 10211

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 1E BD 40 0F 01 1C 04  80 00                    ...@......      
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=-55.107*, Z=104.216*, Y=0.000*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x1E] EventEntity looks at Laila (ID: 17776829/0x010F40BD) and starts talking
  4: 0x0016 [0x1C] WAIT(30* ticks)
  5: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 00 80 1F 00 05            2.....
0020: 80 06 80 03 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-96.208*, Z=170.721*, Y=0.000*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x00] END_REQSTACK()
```
