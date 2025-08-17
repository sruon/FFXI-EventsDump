# 17781028 - Kupolietta

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 624 bytes             |
| Total Events     | 29                    |
| References Count | 13                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     14 |              2 |
| [65535.2](#event-655352)   | 0x000F       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001D       |     14 |              2 |
| [65535.4](#event-655354)   | 0x002B       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0039       |     14 |              2 |
| [65535.6](#event-655356)   | 0x0047       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0055       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0063       |     14 |              2 |
| [65535.9](#event-655359)   | 0x0071       |     14 |              2 |
| [65535.10](#event-6553510) | 0x007F       |     14 |              2 |
| [65535.11](#event-6553511) | 0x008D       |     14 |              2 |
| [65535.12](#event-6553512) | 0x009B       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00A9       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00B7       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00C5       |     14 |              2 |
| [65535.16](#event-6553516) | 0x00D3       |     14 |              2 |
| [65535.17](#event-6553517) | 0x00E1       |     14 |              2 |
| [65535.18](#event-6553518) | 0x00EF       |     14 |              2 |
| [65535.19](#event-6553519) | 0x00FD       |     14 |              2 |
| [65535.20](#event-6553520) | 0x010B       |     14 |              2 |
| [65535.21](#event-6553521) | 0x0119       |     14 |              2 |
| [65535.22](#event-6553522) | 0x0127       |     14 |              2 |
| [65535.23](#event-6553523) | 0x0135       |     14 |              2 |
| [65535.24](#event-6553524) | 0x0143       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0151       |     38 |              5 |
| [20089](#event-20089)      | 0x0177       |      7 |              2 |
| [65535.26](#event-6553526) | 0x017E       |     33 |             11 |
| [65535.27](#event-6553527) | 0x019F       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0xFFFECDE1  |  4294888929 |
|       2 | 0xFFFD62C7  |  4294795975 |
|       3 | 0xFFFFE82B  |  4294961195 |
|       4 | 0xFFFED3BE  |  4294890430 |
|       5 | 0xFFFD6928  |  4294797608 |
|       6 | 0xFFFFE82C  |  4294961196 |
|       7 | 0xFFFECEBF  |  4294889151 |
|       8 | 0xFFFD6651  |  4294796881 |
|       9 | 0xFFFFE82D  |  4294961197 |
|      10 | 0xFFFEB6CF  |  4294883023 |
|      11 | 0xFFFD71C3  |  4294799811 |
|      12 | 0xFFFFE890  |  4294961296 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    2C F8 FF FF 7F F8 FF  FF 7F 6E 6F 30 30 00      ,........no00. 
```

#### Opcodes

```
  0: 0x0001 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "no00" with entities [EventEntity, EventEntity]
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               53                 S
0010: F8 FF FF 7F F8 FF FF 7F  6E 6F 30 30 00           ........no00.   
```

#### Opcodes

```
  0: 0x000F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "no00" with entities [EventEntity, EventEntity]
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         2C F8 FF               ,..
0020: FF 7F F8 FF FF 7F 6B 79  6F 30 00                 ......kyo0.     
```

#### Opcodes

```
  0: 0x001D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kyo0" with entities [EventEntity, EventEntity]
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   53 F8 FF FF 7F             S....
0030: F8 FF FF 7F 6B 79 6F 30  00                       ....kyo0.       
```

#### Opcodes

```
  0: 0x002B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kyo0" with entities [EventEntity, EventEntity]
  1: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             2C F8 FF FF 7F F8 FF           ,......
0040: FF 7F 79 65 73 30 00                              ..yes0.         
```

#### Opcodes

```
  0: 0x0039 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "yes0" with entities [EventEntity, EventEntity]
  1: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0050: 79 65 73 30 00                                    yes0.           
```

#### Opcodes

```
  0: 0x0047 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "yes0" with entities [EventEntity, EventEntity]
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                2C F8 FF  FF 7F F8 FF FF 7F 65 69       ,........ei
0060: 6F 30 00                                          o0.             
```

#### Opcodes

```
  0: 0x0055 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "eio0" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          53 F8 FF FF 7F  F8 FF FF 7F 65 69 6F 30     S........eio0
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0063 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "eio0" with entities [EventEntity, EventEntity]
  1: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    2C F8 FF FF 7F F8 FF  FF 7F 6B 73 75 30 00      ,........ksu0. 
```

#### Opcodes

```
  0: 0x0071 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "ksu0" with entities [EventEntity, EventEntity]
  1: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               53                 S
0080: F8 FF FF 7F F8 FF FF 7F  6B 73 75 30 00           ........ksu0.   
```

#### Opcodes

```
  0: 0x007F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ksu0" with entities [EventEntity, EventEntity]
  1: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         2C F8 FF               ,..
0090: FF 7F F8 FF FF 7F 67 61  6B 30 00                 ......gak0.     
```

#### Opcodes

```
  0: 0x008D [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak0" with entities [EventEntity, EventEntity]
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   53 F8 FF FF 7F             S....
00A0: F8 FF FF 7F 67 61 6B 30  00                       ....gak0.       
```

#### Opcodes

```
  0: 0x009B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak0" with entities [EventEntity, EventEntity]
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             2C F8 FF FF 7F F8 FF           ,......
00B0: FF 7F 67 61 6B 31 00                              ..gak1.         
```

#### Opcodes

```
  0: 0x00A9 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "gak1" with entities [EventEntity, EventEntity]
  1: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      53  F8 FF FF 7F F8 FF FF 7F         S........
00C0: 67 61 6B 31 00                                    gak1.           
```

#### Opcodes

```
  0: 0x00B7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gak1" with entities [EventEntity, EventEntity]
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                2C F8 FF  FF 7F F8 FF FF 7F 74 6C       ,........tl
00D0: 6B 30 00                                          k0.             
```

#### Opcodes

```
  0: 0x00C5 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          53 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30     S........tlk0
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00D3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    2C F8 FF FF 7F F8 FF  FF 7F 68 61 70 30 00      ,........hap0. 
```

#### Opcodes

```
  0: 0x00E1 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "hap0" with entities [EventEntity, EventEntity]
  1: 0x00EE [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EF   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               53                 S
00F0: F8 FF FF 7F F8 FF FF 7F  68 61 70 30 00           ........hap0.   
```

#### Opcodes

```
  0: 0x00EF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hap0" with entities [EventEntity, EventEntity]
  1: 0x00FC [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FD   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                         2C F8 FF               ,..
0100: FF 7F F8 FF FF 7F 6B 72  75 30 00                 ......kru0.     
```

#### Opcodes

```
  0: 0x00FD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kru0" with entities [EventEntity, EventEntity]
  1: 0x010A [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   53 F8 FF FF 7F             S....
0110: F8 FF FF 7F 6B 72 75 30  00                       ....kru0.       
```

#### Opcodes

```
  0: 0x010B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kru0" with entities [EventEntity, EventEntity]
  1: 0x0118 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0119   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                             2C F8 FF FF 7F F8 FF           ,......
0120: FF 7F 73 74 64 30 00                              ..std0.         
```

#### Opcodes

```
  0: 0x0119 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "std0" with entities [EventEntity, EventEntity]
  1: 0x0126 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0127   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0130: 73 74 64 30 00                                    std0.           
```

#### Opcodes

```
  0: 0x0127 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "std0" with entities [EventEntity, EventEntity]
  1: 0x0134 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0135   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                2C F8 FF  FF 7F F8 FF FF 7F 70 6E       ,........pn
0140: 63 30 00                                          c0.             
```

#### Opcodes

```
  0: 0x0135 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "pnc0" with entities [EventEntity, EventEntity]
  1: 0x0142 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0143   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:          53 F8 FF FF 7F  F8 FF FF 7F 70 6E 63 30     S........pnc0
0150: 00                                                .               
```

#### Opcodes

```
  0: 0x0143 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pnc0" with entities [EventEntity, EventEntity]
  1: 0x0150 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0151   |
| Data Size    | 38 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:    4E 00 F8 FF FF 7F 80  F8 FF FF 7F 2C F8 FF FF   N..........,...
0160: 7F F8 FF FF 7F 6B 69 6C  61 53 F8 FF FF 7F F8 FF  .....kilaS......
0170: FF 7F 6B 69 6C 61 00                              ..kila.         
```

#### Opcodes

```
  0: 0x0151 [0x4E] SET_ENTITY_HIDE_FLAG: Show EventEntity
  1: 0x0157 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x015C [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "kila" with entities [EventEntity, EventEntity]
  3: 0x0169 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kila" with entities [EventEntity, EventEntity]
  4: 0x0176 [0x00] END_REQSTACK()
```

### Event 20089

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0177  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0177 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x017D [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017E   |
| Data Size    | 33 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                            32 00                2.
0180: 80 1F 00 01 80 02 80 03  80 1F 01 6F 1F 00 04 80  ...........o....
0190: 05 80 06 80 1F 01 6F 1E  23 51 0F 01 6F 70 00     ......o.#Q..op. 
```

#### Opcodes

```
  0: 0x017E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0181 [0x1F] MOVE_ENTITY: EventEntity moves to X=-78.367*, Z=-171.321*, Y=-6.101*
  2: 0x0189 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x018B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x018C [0x1F] MOVE_ENTITY: EventEntity moves to X=-76.866*, Z=-169.688*, Y=-6.100*
  5: 0x0194 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0196 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0197 [0x1E] EventEntity looks at Mumor (ID: 17781027/0x010F5123) and starts talking
  8: 0x019C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x019D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x019E [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019F   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                               32                 2
01A0: 00 80 1F 00 07 80 08 80  09 80 1F 01 1F 00 0A 80  ................
01B0: 0B 80 0C 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x019F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x01A2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-78.145*, Z=-170.415*, Y=-6.099*
  2: 0x01AA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01AC [0x1F] MOVE_ENTITY: EventEntity moves to X=-84.273*, Z=-167.485*, Y=-6.000*
  4: 0x01B4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x01B6 [0x00] END_REQSTACK()
```
