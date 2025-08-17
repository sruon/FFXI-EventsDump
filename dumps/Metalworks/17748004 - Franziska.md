# 17748004 - Franziska

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 260 bytes            |
| Total Events     | 11                   |
| References Count | 15                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [620](#event-620)        | 0x0001       |     11 |              5 |
| [779](#event-779)        | 0x000C       |     11 |              5 |
| [777](#event-777)        | 0x0017       |     10 |              2 |
| [65535.1](#event-655351) | 0x0021       |     19 |              5 |
| [65535.2](#event-655352) | 0x0034       |     38 |              8 |
| [765](#event-765)        | 0x005A       |      1 |              1 |
| [65535.3](#event-655353) | 0x005B       |     38 |              8 |
| [770](#event-770)        | 0x0081       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F1F      |        7967 |
|       1 | 0x22BD      |        8893 |
|       2 | 0x1BFF5     |      114677 |
|       3 | 0xFFFFD9D9  |  4294957529 |
|       4 | 0xFFFFB136  |  4294947126 |
|       5 | 0x0C0E      |        3086 |
|       6 | 0x000D      |          13 |
|       7 | 0x1C0BD     |      114877 |
|       8 | 0xFFFFDDC1  |  4294958529 |
|       9 | 0x1B7C0     |      112576 |
|      10 | 0xFFFFDBA0  |  4294957984 |
|      11 | 0x0000      |           0 |
|      12 | 0x0078      |         120 |
|      13 | 0xFFFFDAD8  |  4294957784 |
|      14 | 0x222C      |        8748 |

## String References

- **7967**: Lady Cornelia is not here at the moment. I hope she doesn't stay out too late...
- **8748**: Lady Cornelia has locked herself in her room and will not come out...
- **8893**: Recently, Lady Cornelia has taken up an interest in her studies. However, how long this will last, I do not know...

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

### Event 620

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7967*)
    → "Lady Cornelia is not here at the moment. I hope she doesn't stay out too late..."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 779

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=8893*)
    → "Recently, Lady Cornelia has taken up an interest in her studies. However, how long this will last, I do not know..."
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x21] END_EVENT
  4: 0x0016 [0x00] END_REQSTACK()
```

### Event 777

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      37  02 80 03 80 04 80 05 80         7........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=114.677*, z=-9.767*, y=-20.170*, direction=271.2°*
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 06 80 1F 00 07 80  08 80 04 80 1F 01 1E 32   2.............2
0030: D0 0E 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=114.877*, Z=-8.767*, Y=-20.170*
  2: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002E [0x1E] EventEntity looks at Cornelia (ID: 17748018/0x010ED032) and starts talking
  4: 0x0033 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             32 06 80 1F  00 09 80 0A 80 04 80 1F      2...........
0040: 01 6F 5B 0B 80 24 D0 0E  01 24 D0 0E 01 74 6C 6B  .o[..$...$...tlk
0050: 30 1C 0C 80 5E 69 64 6C  30 00                    0...^idl0.      
```

#### Opcodes

```
  0: 0x0034 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=112.576*, Z=-9.312*, Y=-20.170*
  2: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0042 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Franziska (ID: 17748004/0x010ED024), Franziska (ID: 17748004/0x010ED024)], work=0*
  5: 0x0051 [0x1C] WAIT(120* ticks)
  6: 0x0054 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0059 [0x00] END_REQSTACK()
```

### Event 765

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                00                           .     
```

#### Opcodes

```
  0: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   32 06 80 1F 00             2....
0060: 09 80 0D 80 04 80 1F 01  6F 5B 0B 80 24 D0 0E 01  ........o[..$...
0070: 24 D0 0E 01 74 6C 6B 30  1C 0C 80 5E 69 64 6C 30  $...tlk0...^idl0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x005B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=112.576*, Z=-9.512*, Y=-20.170*
  2: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0068 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0069 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Franziska (ID: 17748004/0x010ED024), Franziska (ID: 17748004/0x010ED024)], work=0*
  5: 0x0078 [0x1C] WAIT(120* ticks)
  6: 0x007B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0080 [0x00] END_REQSTACK()
```

### Event 770

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    1E F0 FF FF 7F 1D 0E  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0081 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0086 [0x1D] PRINT_EVENT_MESSAGE(message_id=8748*)
    → "Lady Cornelia has locked herself in her room and will not come out..."
  2: 0x0089 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x008A [0x21] END_EVENT
  4: 0x008B [0x00] END_REQSTACK()
```
