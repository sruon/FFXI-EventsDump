# 17179330 - Mham Lahrih

## Common Data

| Field            | Value                             |
|------------------|-----------------------------------|
| Zone             | Sauromugue Champaign [S] (ID: 98) |
| Block Size       | 180 bytes                         |
| Total Events     | 5                                 |
| References Count | 6                                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [109](#event-109)     | 0x0001       |      1 |              1 |
| [113](#event-113)     | 0x0002       |      1 |              1 |
| [111](#event-111)     | 0x0003       |     65 |             11 |
| [112](#event-112)     | 0x0044       |     52 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x041A      |        1050 |
|       2 | 0x003B      |          59 |
|       3 | 0x1F1A      |        7962 |
|       4 | 0x1F1B      |        7963 |
|       5 | 0x1F1C      |        7964 |

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

### Event 109

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

### Event 113

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

### Event 111

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 65 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          4A F8 FF FF 7F  F0 FF FF 7F 1C 00 80 03     J............
0010: 02 10 01 80 66 02 80 F8  FF FF 7F F8 FF FF 7F 74  ....f..........t
0020: 6C 6B 30 2B F8 FF FF 7F  03 80 23 2B F8 FF FF 7F  lk0+......#+....
0030: 04 80 23 66 02 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0040: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x0003 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000C [0x1C] WAIT(30* ticks)
  2: 0x000F [0x03] Work_Zone[2] = 1050*
  3: 0x0014 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  4: 0x0023 [0x2B] EventEntity [7962*]:
    → "Hey, you must be <Player>. Lehko's told me about the strrrategy."
  5: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002B [0x2B] EventEntity [7963*]:
    → "Here's a spare $3. Now, go and show them Gigas a trrrick or two!"
  7: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0033 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  9: 0x0042 [0x21] END_EVENT
 10: 0x0043 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 52 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             4A F8 FF FF  7F F0 FF FF 7F 1C 00 80      J...........
0050: 66 02 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 2B  f..........tlk0+
0060: F8 FF FF 7F 05 80 23 66  02 80 F8 FF FF 7F F8 FF  ......#f........
0070: FF 7F 74 6C 6B 31 21 00                           ..tlk1!.        
```

#### Opcodes

```
  0: 0x0044 [0x4A] EventEntity looks at LocalPlayer
  1: 0x004D [0x1C] WAIT(30* ticks)
  2: 0x0050 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=59*
  3: 0x005F [0x2B] EventEntity [7964*]:
    → "What is it? The battle's rrraging, so if you don't want to take a stray arrow where the sun don't shine, stay on your toes."
  4: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0067 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=59*
  6: 0x0076 [0x21] END_EVENT
  7: 0x0077 [0x00] END_REQSTACK()
```
