# 17453359 - Garazu-Horeizu

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Throne Room (ID: 165) |
| Block Size       | 684 bytes             |
| Total Events     | 32                    |
| References Count | 8                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [32001](#event-32001)      | 0x0001       |      7 |              2 |
| [65535.1](#event-655351)   | 0x0008       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0018       |     14 |              2 |
| [65535.3](#event-655353)   | 0x0026       |     22 |              3 |
| [65535.4](#event-655354)   | 0x003C       |     14 |              2 |
| [65535.5](#event-655355)   | 0x004A       |     22 |              3 |
| [65535.6](#event-655356)   | 0x0060       |     14 |              2 |
| [65535.7](#event-655357)   | 0x006E       |     16 |              2 |
| [65535.8](#event-655358)   | 0x007E       |     14 |              2 |
| [65535.9](#event-655359)   | 0x008C       |     16 |              2 |
| [65535.10](#event-6553510) | 0x009C       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00AA       |     28 |              4 |
| [65535.12](#event-6553512) | 0x00C6       |     14 |              2 |
| [65535.13](#event-6553513) | 0x00D4       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00E4       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00F2       |     16 |              2 |
| [65535.16](#event-6553516) | 0x0102       |     14 |              2 |
| [65535.17](#event-6553517) | 0x0110       |     16 |              2 |
| [65535.18](#event-6553518) | 0x0120       |     14 |              2 |
| [65535.19](#event-6553519) | 0x012E       |     16 |              2 |
| [65535.20](#event-6553520) | 0x013E       |     14 |              2 |
| [65535.21](#event-6553521) | 0x014C       |     16 |              2 |
| [65535.22](#event-6553522) | 0x015C       |     14 |              2 |
| [65535.23](#event-6553523) | 0x016A       |     16 |              2 |
| [65535.24](#event-6553524) | 0x017A       |     14 |              2 |
| [65535.25](#event-6553525) | 0x0188       |     22 |              3 |
| [65535.26](#event-6553526) | 0x019E       |     20 |              3 |
| [65535.27](#event-6553527) | 0x01B2       |     16 |              2 |
| [65535.28](#event-6553528) | 0x01C2       |     14 |              2 |
| [65535.29](#event-6553529) | 0x01D0       |     22 |              3 |
| [65535.30](#event-6553530) | 0x01E6       |     20 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0809      |        2057 |
|       1 | 0x00B7      |         183 |
|       2 | 0x0805      |        2053 |
|       3 | 0x006F      |         111 |
|       4 | 0x0070      |         112 |
|       5 | 0x0808      |        2056 |
|       6 | 0x0804      |        2052 |
|       7 | 0x00A6      |         166 |

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

### Event 32001

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
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          5B 00 80 F8 FF FF 7F F8          [.......
0010: FF FF 7F 6B 61 7A 65 00                           ...kaze.        
```

#### Opcodes

```
  0: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kaze" with entities [EventEntity, EventEntity], work=2057*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          53 F8 FF FF 7F F8 FF FF          S.......
0020: 7F 6B 61 7A 65 00                                 .kaze.          
```

#### Opcodes

```
  0: 0x0018 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kaze" with entities [EventEntity, EventEntity]
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   81 00  F8 FF FF 7F 66 01 80 F8        ......f...
0030: FF FF 7F F8 FF FF 7F 77  6E 64 30 00              .......wnd0.    
```

#### Opcodes

```
  0: 0x0026 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "wnd0" with entities [EventEntity, EventEntity], work=183*
  2: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      53 F8 FF FF              S...
0040: 7F F8 FF FF 7F 77 6E 64  30 00                    .....wnd0.      
```

#### Opcodes

```
  0: 0x003C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "wnd0" with entities [EventEntity, EventEntity]
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                81 00 F8 FF FF 7F            ......
0050: 66 01 80 F8 FF FF 7F F8  FF FF 7F 68 6E 64 30 00  f..........hnd0.
```

#### Opcodes

```
  0: 0x004A [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0050 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "hnd0" with entities [EventEntity, EventEntity], work=183*
  2: 0x005F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0060   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060: 53 F8 FF FF 7F F8 FF FF  7F 68 6E 64 30 00        S........hnd0.  
```

#### Opcodes

```
  0: 0x0060 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hnd0" with entities [EventEntity, EventEntity]
  1: 0x006D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            5B 02                [.
0070: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 68 30 00        .........tlh0.  
```

#### Opcodes

```
  0: 0x006E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlh0" with entities [EventEntity, EventEntity], work=2053*
  1: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            53 F8                S.
0080: FF FF 7F F8 FF FF 7F 74  6C 68 30 00              .......tlh0.    
```

#### Opcodes

```
  0: 0x007E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlh0" with entities [EventEntity, EventEntity]
  1: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      5B 02 80 F8              [...
0090: FF FF 7F F8 FF FF 7F 74  6C 72 30 00              .......tlr0.    
```

#### Opcodes

```
  0: 0x008C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlr0" with entities [EventEntity, EventEntity], work=2053*
  1: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      53 F8 FF FF              S...
00A0: 7F F8 FF FF 7F 74 6C 72  30 00                    .....tlr0.      
```

#### Opcodes

```
  0: 0x009C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlr0" with entities [EventEntity, EventEntity]
  1: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                81 00 F8 FF FF 7F            ......
00B0: 7C 00 F8 FF FF 7F 5B 02  80 F8 FF FF 7F F8 FF FF  |.....[.........
00C0: 7F 73 69 6E 30 00                                 .sin0.          
```

#### Opcodes

```
  0: 0x00AA [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x00B0 [0x7C] EventEntity->Render.Flags2 |= 0x00
  2: 0x00B6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sin0" with entities [EventEntity, EventEntity], work=2053*
  3: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   53 F8  FF FF 7F F8 FF FF 7F 73        S........s
00D0: 69 6E 30 00                                       in0.            
```

#### Opcodes

```
  0: 0x00C6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sin0" with entities [EventEntity, EventEntity]
  1: 0x00D3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D4   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             66 03 80 F8  FF FF 7F F8 FF FF 7F 6C      f..........l
00E0: 6C 7A 30 00                                       lz0.            
```

#### Opcodes

```
  0: 0x00D4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "llz0" with entities [EventEntity, EventEntity], work=111*
  1: 0x00E3 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             53 F8 FF FF  7F F8 FF FF 7F 6C 6C 7A      S........llz
00F0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x00E4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "llz0" with entities [EventEntity, EventEntity]
  1: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       66 04 80 F8 FF FF  7F F8 FF FF 7F 65 63 61    f..........eca
0100: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x00F2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "eca0" with entities [EventEntity, EventEntity], work=112*
  1: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       53 F8 FF FF 7F F8  FF FF 7F 65 63 61 30 00    S........eca0.
```

#### Opcodes

```
  0: 0x0102 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "eca0" with entities [EventEntity, EventEntity]
  1: 0x010F [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0110   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 66 04 80 F8 FF FF 7F F8  FF FF 7F 65 63 61 31 00  f..........eca1.
```

#### Opcodes

```
  0: 0x0110 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "eca1" with entities [EventEntity, EventEntity], work=112*
  1: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 53 F8 FF FF 7F F8 FF FF  7F 65 63 61 31 00        S........eca1.  
```

#### Opcodes

```
  0: 0x0120 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "eca1" with entities [EventEntity, EventEntity]
  1: 0x012D [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012E   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                            5B 05                [.
0130: 80 F8 FF FF 7F F8 FF FF  7F 6B 72 61 31 00        .........kra1.  
```

#### Opcodes

```
  0: 0x012E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kra1" with entities [EventEntity, EventEntity], work=2056*
  1: 0x013D [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            53 F8                S.
0140: FF FF 7F F8 FF FF 7F 6B  72 61 31 00              .......kra1.    
```

#### Opcodes

```
  0: 0x013E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kra1" with entities [EventEntity, EventEntity]
  1: 0x014B [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                      5B 06 80 F8              [...
0150: FF FF 7F F8 FF FF 7F 68  69 7A 31 00              .......hiz1.    
```

#### Opcodes

```
  0: 0x014C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hiz1" with entities [EventEntity, EventEntity], work=2052*
  1: 0x015B [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                      53 F8 FF FF              S...
0160: 7F F8 FF FF 7F 68 69 7A  31 00                    .....hiz1.      
```

#### Opcodes

```
  0: 0x015C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hiz1" with entities [EventEntity, EventEntity]
  1: 0x0169 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                5B 07 80 F8 FF FF            [.....
0170: 7F F8 FF FF 7F 6B 73 77  30 00                    .....ksw0.      
```

#### Opcodes

```
  0: 0x016A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ksw0" with entities [EventEntity, EventEntity], work=166*
  1: 0x0179 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                53 F8 FF FF 7F F8            S.....
0180: FF FF 7F 6B 73 77 30 00                           ...ksw0.        
```

#### Opcodes

```
  0: 0x017A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ksw0" with entities [EventEntity, EventEntity]
  1: 0x0187 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0188   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                          81 00 F8 FF FF 7F 5B 07          ......[.
0190: 80 F8 FF FF 7F F8 FF FF  7F 6B 73 74 30 00        .........kst0.  
```

#### Opcodes

```
  0: 0x0188 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x018E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kst0" with entities [EventEntity, EventEntity], work=166*
  2: 0x019D [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x019E   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                                            53 F8                S.
01A0: FF FF 7F F8 FF FF 7F 6B  73 74 30 81 01 F8 FF FF  .......kst0.....
01B0: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x019E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kst0" with entities [EventEntity, EventEntity]
  1: 0x01AB [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x01B1 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:       5B 07 80 F8 FF FF  7F F8 FF FF 7F 6B 73 74    [..........kst
01C0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x01B2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kst1" with entities [EventEntity, EventEntity], work=166*
  1: 0x01C1 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C2   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:       53 F8 FF FF 7F F8  FF FF 7F 6B 73 74 31 00    S........kst1.
```

#### Opcodes

```
  0: 0x01C2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kst1" with entities [EventEntity, EventEntity]
  1: 0x01CF [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D0   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0: 81 00 F8 FF FF 7F 5B 07  80 F8 FF FF 7F F8 FF FF  ......[.........
01E0: 7F 6B 75 70 30 00                                 .kup0.          
```

#### Opcodes

```
  0: 0x01D0 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x01D6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "kup0" with entities [EventEntity, EventEntity], work=166*
  2: 0x01E5 [0x00] END_REQSTACK()
```

### Event 65535.30

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E6   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:                   53 F8  FF FF 7F F8 FF FF 7F 6B        S........k
01F0: 75 70 30 81 01 F8 FF FF  7F 00                    up0.......      
```

#### Opcodes

```
  0: 0x01E6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "kup0" with entities [EventEntity, EventEntity]
  1: 0x01F3 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x01F9 [0x00] END_REQSTACK()
```
