# 17830152 - Estienneux

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 668 bytes                 |
| Total Events     | 18                        |
| References Count | 16                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [98](#event-98)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     41 |             11 |
| [65535.2](#event-655352)   | 0x002B       |     19 |              5 |
| [65535.3](#event-655353)   | 0x003E       |     24 |              5 |
| [65535.4](#event-655354)   | 0x0056       |     33 |              3 |
| [65535.5](#event-655355)   | 0x0077       |     33 |              3 |
| [65535.6](#event-655356)   | 0x0098       |     33 |              3 |
| [65535.7](#event-655357)   | 0x00B9       |     33 |              3 |
| [65535.8](#event-655358)   | 0x00DA       |     33 |              3 |
| [65535.9](#event-655359)   | 0x00FB       |     33 |              3 |
| [65535.10](#event-6553510) | 0x011C       |     33 |              3 |
| [65535.11](#event-6553511) | 0x013D       |     33 |              3 |
| [65535.12](#event-6553512) | 0x015E       |     33 |              3 |
| [65535.13](#event-6553513) | 0x017F       |     33 |              3 |
| [65535.14](#event-6553514) | 0x01A0       |     33 |              3 |
| [65535.15](#event-6553515) | 0x01C1       |     33 |              3 |
| [65535.16](#event-6553516) | 0x01E2       |     33 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFF765  |  4294965093 |
|       2 | 0x1065      |        4197 |
|       3 | 0x0000      |           0 |
|       4 | 0xFFFFF81B  |  4294965275 |
|       5 | 0x085A      |        2138 |
|       6 | 0x003D      |          61 |
|       7 | 0xFFFFFE5A  |  4294966874 |
|       8 | 0x003A      |          58 |
|       9 | 0x0622      |        1570 |
|      10 | 0x0014      |          20 |
|      11 | 0x0064      |         100 |
|      12 | 0x001B      |          27 |
|      13 | 0x0042      |          66 |
|      14 | 0x001A      |          26 |
|      15 | 0x0015      |          21 |

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

### Event 98

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 41 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 03 80 1F  01 1F 00 06 80 07 80 03  ................
0020: 80 1F 01 1E F0 FF FF 7F  6F 70 00                 ........op.     
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.203*, Z=4.197*, Y=0.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-2.021*, Z=2.138*, Y=0.000*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.061*, Z=-0.422*, Y=0.000*
  6: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  8: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0029 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   7B F8 FF FF 7F             {....
0030: 32 00 80 1F 00 08 80 09  80 03 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x002B [0x7B] EventEntity stops talking
  1: 0x0030 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.058*, Z=1.570*, Y=0.000*
  3: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            79 00                y.
0040: F8 FF FF 7F F0 FF FF 7F  32 00 80 1F 00 06 80 07  ........2.......
0050: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x003E [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x0048 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=0.061*, Z=-0.422*, Y=0.000*
  3: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   5F 06  0A 80 F8 FF FF 7F F8 FF        _.........
0060: FF 7F 74 6C 6B 30 0B 80  5F 07 F8 FF FF 7F F8 FF  ..tlk0.._.......
0070: FF 7F 74 6C 6B 30 00                              ..tlk0.         
```

#### Opcodes

```
  0: 0x0056 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=20*, entity1=EventEntity, entity2=EventEntity, string="tlk0", extra=100*)
  1: 0x0068 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      5F  06 0A 80 F8 FF FF 7F F8         _........
0080: FF FF 7F 74 6C 6B 31 0B  80 5F 07 F8 FF FF 7F F8  ...tlk1.._......
0090: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x0077 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=20*, entity1=EventEntity, entity2=EventEntity, string="tlk1", extra=100*)
  1: 0x0089 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0098   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          5F 06 0A 80 F8 FF FF 7F          _.......
00A0: F8 FF FF 7F 74 68 6B 31  0B 80 5F 07 F8 FF FF 7F  ....thk1.._.....
00B0: F8 FF FF 7F 74 68 6B 31  00                       ....thk1.       
```

#### Opcodes

```
  0: 0x0098 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=20*, entity1=EventEntity, entity2=EventEntity, string="thk1", extra=100*)
  1: 0x00AA [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             5F 06 0A 80 F8 FF FF           _......
00C0: 7F F8 FF FF 7F 74 68 6B  32 0B 80 5F 07 F8 FF FF  .....thk2.._....
00D0: 7F F8 FF FF 7F 74 68 6B  32 00                    .....thk2.      
```

#### Opcodes

```
  0: 0x00B9 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=20*, entity1=EventEntity, entity2=EventEntity, string="thk2", extra=100*)
  1: 0x00CB [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00D9 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DA   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                5F 06 0C 80 F8 FF            _.....
00E0: FF 7F F8 FF FF 7F 74 6C  62 30 0B 80 5F 07 F8 FF  ......tlb0.._...
00F0: FF 7F F8 FF FF 7F 74 6C  62 30 00                 ......tlb0.     
```

#### Opcodes

```
  0: 0x00DA [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=27*, entity1=EventEntity, entity2=EventEntity, string="tlb0", extra=100*)
  1: 0x00EC [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x00FA [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   5F 06 0C 80 F8             _....
0100: FF FF 7F F8 FF FF 7F 74  6C 62 31 0B 80 5F 07 F8  .......tlb1.._..
0110: FF FF 7F F8 FF FF 7F 74  6C 62 31 00              .......tlb1.    
```

#### Opcodes

```
  0: 0x00FB [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=27*, entity1=EventEntity, entity2=EventEntity, string="tlb1", extra=100*)
  1: 0x010D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x011B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011C   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      5F 06 0D 80              _...
0120: F8 FF FF 7F F8 FF FF 7F  73 74 64 30 0B 80 5F 07  ........std0.._.
0130: F8 FF FF 7F F8 FF FF 7F  73 74 64 30 00           ........std0.   
```

#### Opcodes

```
  0: 0x011C [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=66*, entity1=EventEntity, entity2=EventEntity, string="std0", extra=100*)
  1: 0x012E [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x013C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013D   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         5F 06 0D               _..
0140: 80 F8 FF FF 7F F8 FF FF  7F 73 74 64 31 0B 80 5F  .........std1.._
0150: 07 F8 FF FF 7F F8 FF FF  7F 73 74 64 31 00        .........std1.  
```

#### Opcodes

```
  0: 0x013D [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=66*, entity1=EventEntity, entity2=EventEntity, string="std1", extra=100*)
  1: 0x014F [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x015D [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015E   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                            5F 06                _.
0160: 0D 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 63 30 0B 80  ..........tlc0..
0170: 5F 07 F8 FF FF 7F F8 FF  FF 7F 74 6C 63 30 00     _.........tlc0. 
```

#### Opcodes

```
  0: 0x015E [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=66*, entity1=EventEntity, entity2=EventEntity, string="tlc0", extra=100*)
  1: 0x0170 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x017E [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017F   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                               5F                 _
0180: 06 0D 80 F8 FF FF 7F F8  FF FF 7F 74 6C 63 31 0B  ...........tlc1.
0190: 80 5F 07 F8 FF FF 7F F8  FF FF 7F 74 6C 63 31 00  ._.........tlc1.
```

#### Opcodes

```
  0: 0x017F [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=66*, entity1=EventEntity, entity2=EventEntity, string="tlc1", extra=100*)
  1: 0x0191 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x019F [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A0   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0: 5F 06 0E 80 F8 FF FF 7F  F8 FF FF 7F 6F 72 6F 30  _...........oro0
01B0: 0B 80 5F 07 F8 FF FF 7F  F8 FF FF 7F 6F 72 6F 30  .._.........oro0
01C0: 00                                                .               
```

#### Opcodes

```
  0: 0x01A0 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=26*, entity1=EventEntity, entity2=EventEntity, string="oro0", extra=100*)
  1: 0x01B2 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x01C0 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C1   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:    5F 06 0E 80 F8 FF FF  7F F8 FF FF 7F 6F 72 6F   _...........oro
01D0: 31 0B 80 5F 07 F8 FF FF  7F F8 FF FF 7F 6F 72 6F  1.._.........oro
01E0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x01C1 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=26*, entity1=EventEntity, entity2=EventEntity, string="oro1", extra=100*)
  1: 0x01D3 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x01E1 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E2   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:       5F 06 0F 80 F8 FF  FF 7F F8 FF FF 7F 64 69    _...........di
01F0: 73 30 0B 80 5F 07 F8 FF  FF 7F F8 FF FF 7F 64 69  s0.._.........di
0200: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x01E2 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x06 - Load ext scheduler with flag (OpCode 0x5B mode 1, flag 1), ref=21*, entity1=EventEntity, entity2=EventEntity, string="dis0", extra=100*)
  1: 0x01F4 [0x5F] MULTI_HANDLER_COMPLEX(mode=0x07 - Wait scheduler task (OpCode 0x53))
  2: 0x0202 [0x00] END_REQSTACK()
```
