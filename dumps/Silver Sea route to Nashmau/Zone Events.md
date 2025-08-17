# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                                |
|------------------|--------------------------------------|
| Zone             | Silver Sea route to Nashmau (ID: 58) |
| Block Size       | 168 bytes                            |
| Total Events     | 6                                    |
| References Count | 3                                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [1026](#event-1026)   | 0x0002       |     36 |              6 |
| [1025](#event-1025)   | 0x0026       |     26 |              7 |
| [1027](#event-1027)   | 0x0040       |     26 |              7 |
| [1028](#event-1028)   | 0x005A       |     26 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x003C      |          60 |

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

### Event 1026

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 36 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       30 42 45 00 80 F0  FF FF 7F F0 FF FF 7F 66    0BE..........f
0010: 64 6F 32 01 80 55 00 80  F0 FF FF 7F F0 FF FF 7F  do2..U..........
0020: 66 64 6F 32 21 00                                 fdo2!.          
```

#### Opcodes

```
  0: 0x0002 [0x30] SET_UCOFF_CONTINUE_ZERO()
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0015 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
  4: 0x0024 [0x21] END_EVENT
  5: 0x0025 [0x00] END_REQSTACK()
```

### Event 1025

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   20 01  42 45 00 80 F0 FF FF 7F         .BE......
0030: F0 FF FF 7F 66 64 6F 31  01 80 1C 02 80 30 21 00  ....fdo1.....0!.
```

#### Opcodes

```
  0: 0x0026 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0028 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x003A [0x1C] WAIT(60* ticks)
  4: 0x003D [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x003E [0x21] END_EVENT
  6: 0x003F [0x00] END_REQSTACK()
```

### Event 1027

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 20 01 42 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64   .BE..........fd
0050: 6F 31 01 80 1C 02 80 30  21 00                    o1.....0!.      
```

#### Opcodes

```
  0: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0042 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0043 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0054 [0x1C] WAIT(60* ticks)
  4: 0x0057 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x0058 [0x21] END_EVENT
  6: 0x0059 [0x00] END_REQSTACK()
```

### Event 1028

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                20 01 42 45 00 80             .BE..
0060: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 02  ........fdo1....
0070: 80 30 21 00                                       .0!.            
```

#### Opcodes

```
  0: 0x005A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x005C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x005D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x006E [0x1C] WAIT(60* ticks)
  4: 0x0071 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x0072 [0x21] END_EVENT
  6: 0x0073 [0x00] END_REQSTACK()
```
