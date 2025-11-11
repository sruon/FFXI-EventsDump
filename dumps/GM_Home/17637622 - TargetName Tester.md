# 17637622 - TargetName Tester

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 60 bytes          |
| Total Events     | 2                 |
| References Count | 3                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [177](#event-177)     | 0x0001       |     22 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x0000      |           0 |
|       2 | 0x23B7      |        9143 |

## String References

- **9143**: %0

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

### Event 177

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    71 30 00 80 71 31 00  00 71 01 B4 04 00 00 01   q0..q1..q......
0010: 80 1D 02 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x0001 [0x71] USER_INPUT_HANDLER: Menu operation A (param=0x8000)
  1: 0x0005 [0x71] USER_INPUT_HANDLER: Menu operation B (param=0x0000)
  2: 0x0009 [0x71] USER_INPUT_HANDLER: Check if player has input or exited
  3: 0x000B [0xB4] UI_WINDOW_STRING_HANDLER(case=0x04 - Copy string to shared buffers, work_offset1=ExtData[1]->WorkLocal[0], work_offset2=0*)
  4: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=9143*)
    → "%0"
  5: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0015 [0x21] END_EVENT
  7: 0x0016 [0x00] END_REQSTACK()
```
