# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Castle Zvahl Baileys (ID: 161) |
| Block Size       | 396 bytes                      |
| Total Events     | 8                              |
| References Count | 21                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [0](#event-0)            | 0x0002       |     59 |             11 |
| [1](#event-1)            | 0x003D       |     59 |             11 |
| [2](#event-2)            | 0x0078       |     59 |             11 |
| [3](#event-3)            | 0x00B3       |     59 |             11 |
| [65535.1](#event-655351) | 0x00EE       |      9 |              3 |
| [65535.2](#event-655352) | 0x00F7       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x00B4      |         180 |
|       3 | 0x13AA7     |       80551 |
|       4 | 0x26F9D     |      159645 |
|       5 | 0xFFFFE0C0  |  4294959296 |
|       6 | 0x0B1B      |        2843 |
|       7 | 0x0002      |           2 |
|       8 | 0x139F8     |       80376 |
|       9 | 0xFFFE2D7D  |  4294847869 |
|      10 | 0x0C3D      |        3133 |
|      11 | 0xFFFCF30E  |  4294767374 |
|      12 | 0xFFFE2C2B  |  4294847531 |
|      13 | 0x0C0A      |        3082 |
|      14 | 0xFFFCF4FC  |  4294767868 |
|      15 | 0x2723A     |      160314 |
|      16 | 0x0C05      |        3077 |
|      17 | 0x000F      |          15 |
|      18 | 0x5CC83     |      380035 |
|      19 | 0xFFFFB1E0  |  4294947296 |
|      20 | 0xFFFFD120  |  4294955296 |

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

### Event 65534

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

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 59 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 62 00 80  F8 FF FF 7F F8 FF FF 7F     .Bb..........
0010: 6D 61 69 6E 01 80 1C 02  80 47 00 03 80 04 80 05  main.....G......
0020: 80 06 80 47 01 62 07 80  F8 FF FF 7F F8 FF FF 7F  ...G.b..........
0030: 6D 61 69 6E 01 80 1C 02  80 20 00 21 00           main..... .!.   
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[1*, 0*]
  3: 0x0016 [0x1C] WAIT(180* ticks)
  4: 0x0019 [0x47] UPDATE_PLAYER_POS(80.551*, 159.645*, -8.000*, yaw=249.9°*)
  5: 0x0023 [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x0025 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[2*, 0*]
  7: 0x0036 [0x1C] WAIT(180* ticks)
  8: 0x0039 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x003B [0x21] END_EVENT
 10: 0x003C [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 59 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         20 01 42                .B
0040: 62 00 80 F8 FF FF 7F F8  FF FF 7F 6D 61 69 6E 01  b..........main.
0050: 80 1C 02 80 47 00 08 80  09 80 05 80 0A 80 47 01  ....G.........G.
0060: 62 07 80 F8 FF FF 7F F8  FF FF 7F 6D 61 69 6E 01  b..........main.
0070: 80 1C 02 80 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x003D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x003F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0040 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[1*, 0*]
  3: 0x0051 [0x1C] WAIT(180* ticks)
  4: 0x0054 [0x47] UPDATE_PLAYER_POS(80.376*, -119.427*, -8.000*, yaw=275.4°*)
  5: 0x005E [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x0060 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[2*, 0*]
  7: 0x0071 [0x1C] WAIT(180* ticks)
  8: 0x0074 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0076 [0x21] END_EVENT
 10: 0x0077 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 59 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          20 01 42 62 00 80 F8 FF           .Bb....
0080: FF 7F F8 FF FF 7F 6D 61  69 6E 01 80 1C 02 80 47  ......main.....G
0090: 00 0B 80 0C 80 05 80 0D  80 47 01 62 07 80 F8 FF  .........G.b....
00A0: FF 7F F8 FF FF 7F 6D 61  69 6E 01 80 1C 02 80 20  ......main..... 
00B0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0078 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x007A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x007B [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[1*, 0*]
  3: 0x008C [0x1C] WAIT(180* ticks)
  4: 0x008F [0x47] UPDATE_PLAYER_POS(-199.922*, -119.765*, -8.000*, yaw=270.9°*)
  5: 0x0099 [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x009B [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[2*, 0*]
  7: 0x00AC [0x1C] WAIT(180* ticks)
  8: 0x00AF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x00B1 [0x21] END_EVENT
 10: 0x00B2 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B3   |
| Data Size    | 59 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:          20 01 42 62 00  80 F8 FF FF 7F F8 FF FF      .Bb.........
00C0: 7F 6D 61 69 6E 01 80 1C  02 80 47 00 0E 80 0F 80  .main.....G.....
00D0: 05 80 10 80 47 01 62 07  80 F8 FF FF 7F F8 FF FF  ....G.b.........
00E0: 7F 6D 61 69 6E 01 80 1C  02 80 20 00 21 00        .main..... .!.  
```

#### Opcodes

```
  0: 0x00B3 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00B5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00B6 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[1*, 0*]
  3: 0x00C7 [0x1C] WAIT(180* ticks)
  4: 0x00CA [0x47] UPDATE_PLAYER_POS(-199.428*, 160.314*, -8.000*, yaw=270.4°*)
  5: 0x00D4 [0x47] WAIT_PLAYER_POS_UPDATE
  6: 0x00D6 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[2*, 0*]
  7: 0x00E7 [0x1C] WAIT(180* ticks)
  8: 0x00EA [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x00EC [0x21] END_EVENT
 10: 0x00ED [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EE  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                            22 00                ".
00F0: 94 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x00EE [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x00F0 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x00F6 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F7   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                      32  11 80 1F 00 12 80 13 80         2........
0100: 14 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x00F7 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x00FA [0x1F] MOVE_ENTITY: EventEntity moves to X=380.035*, Z=-20.000*, Y=-12.000*
  2: 0x0102 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0104 [0x00] END_REQSTACK()
```
