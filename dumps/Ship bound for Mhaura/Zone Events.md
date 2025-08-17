# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Ship bound for Mhaura (ID: 228) |
| Block Size       | 172 bytes                       |
| Total Events     | 5                               |
| References Count | 4                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [512](#event-512)     | 0x0001       |      8 |              4 |
| [10](#event-10)       | 0x0009       |     39 |              7 |
| [2048](#event-2048)   | 0x0030       |     71 |             11 |
| [65534](#event-65534) | 0x0077       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CB7      |        7351 |
|       1 | 0x1CB9      |        7353 |
|       2 | 0x00C8      |         200 |
|       3 | 0x0000      |           0 |

## String References

- **7351**: We are now docking in Mhaura.
- **7353**: You have entered the ship route by unauthorized means. Zoning you to Selbina.

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

### Event 512

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 8 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 1A 54 00 21  00                        H...T.!.       
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7351*]:
    → "We are now docking in Mhaura."
  1: 0x0004 [0x1A] CALL_SUBROUTINE(address=0x0054)
  2: 0x0007 [0x21] END_EVENT
  3: 0x0008 [0x00] END_REQSTACK()
```

### Event 10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0009   |
| Data Size    | 39 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                             30 42 48 01 80 45 02           0BH..E.
0010: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 30 03 80 55  .........fdo0..U
0020: 02 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 30 21 00  ..........fdo0!.
```

#### Opcodes

```
  0: 0x0009 [0x30] SET_UCOFF_CONTINUE_ZERO()
  1: 0x000A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x000B [0x48] [System] [7353*]:
    → "You have entered the ship route by unauthorized means. Zoning you to Selbina."
  3: 0x000E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x001F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x002E [0x21] END_EVENT
  6: 0x002F [0x00] END_REQSTACK()
```

### Event 2048

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 71 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 30 42 45 02 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  0BE..........fdo
0040: 30 03 80 55 02 80 F0 FF  FF 7F F0 FF FF 7F 66 64  0..U..........fd
0050: 6F 30 21 00 30 42 45 02  80 F0 FF FF 7F F0 FF FF  o0!.0BE.........
0060: 7F 66 64 6F 32 03 80 55  02 80 F0 FF FF 7F F0 FF  .fdo2..U........
0070: FF 7F 66 64 6F 32 1B                              ..fdo2.         
```

#### Opcodes

```
  0: 0x0030 [0x30] SET_UCOFF_CONTINUE_ZERO()
  1: 0x0031 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0032 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0043 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
  4: 0x0052 [0x21] END_EVENT
  5: 0x0053 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0054 [0x30] SET_UCOFF_CONTINUE_ZERO()
     0x0055 [0x42] SET_CLI_EVENT_CANCEL_DATA()
     0x0056 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0067 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0076 [0x1B] RETURN
```

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0077  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      00                                  .        
```

#### Opcodes

```
  0: 0x0077 [0x00] END_REQSTACK()
```
