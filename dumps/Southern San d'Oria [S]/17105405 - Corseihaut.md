# 17105405 - Corseihaut

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 88 bytes                         |
| Total Events     | 3                                |
| References Count | 3                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [610](#event-610)     | 0x0001       |     45 |              9 |
| [128](#event-128)     | 0x002E       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001D      |          29 |
|       1 | 0x2F4D      |       12109 |
|       2 | 0x2F4E      |       12110 |

## String References

- **12109**: My word, those forsaken Royal Knights... It was bad enough when I heard they were scavenging the broken weapons of the Orcs, but now they are leaving them strewn about the city!
- **12110**: I don't know if they intend to study them or use them as toys for our children! All I do know is that we Temple Knights will have to clean up their mess, as always!

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

### Event 610

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 45 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 66 00  80 FD 01 05 01 FD 01 05   .....f.........
0010: 01 74 6C 6B 30 1D 01 80  23 1D 02 80 23 66 00 80  .tlk0...#...#f..
0020: FD 01 05 01 FD 01 05 01  74 6C 6B 31 21 00        ........tlk1!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Corseihaut (ID: 17105405/0x010501FD), Corseihaut (ID: 17105405/0x010501FD)], work=29*
  2: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=12109*)
    → "My word, those forsaken Royal Knights... It was bad enough when I heard they were scavenging the broken weapons of the Orcs, but now they are leaving them strewn about the city!"
  3: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=12110*)
    → "I don't know if they intend to study them or use them as toys for our children! All I do know is that we Temple Knights will have to clean up their mess, as always!"
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Corseihaut (ID: 17105405/0x010501FD), Corseihaut (ID: 17105405/0x010501FD)], work=29*
  7: 0x002C [0x21] END_EVENT
  8: 0x002D [0x00] END_REQSTACK()
```

### Event 128

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```
