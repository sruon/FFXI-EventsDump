# 17727517 - Meinemelle

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 132 bytes                 |
| Total Events     | 3                         |
| References Count | 6                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [500](#event-500)     | 0x0001       |      1 |              1 |
| [544](#event-544)     | 0x0002       |     76 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1F31      |        7985 |
|       2 | 0x1F32      |        7986 |
|       3 | 0x0000      |           0 |
|       4 | 0x0001      |           1 |
|       5 | 0x40000000  |  1073741824 |

## String References

- **7985**: Now delivering parcels to rooms everywhere!
- **7986**: Send? [Yes./Not now.]

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

### Event 500

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

### Event 544

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 76 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F    .....opf......
0010: F8 FF FF 7F 74 6C 6B 30  1D 01 80 23 5E 69 64 6C  ....tlk0...#^idl
0020: 30 24 02 80 03 80 03 80  25 02 00 10 03 80 00 39  0$......%......9
0030: 00 03 01 10 03 80 01 49  00 02 00 10 04 80 00 49  .......I.......I
0040: 00 03 01 10 05 80 01 49  00 1C 00 80 21 00        .......I....!.  
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7985*)
    → "Now delivering parcels to rooms everywhere!"
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  7: 0x0021 [0x24] CREATE_DIALOG(message_id=7986*, default_option=0*, option_flags=0*)
    → "Send? [Yes./Not now.]"
  8: 0x0028 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0029 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0039
 10: 0x0031 [0x03] Work_Zone[1] = 0*
 11: 0x0036 [0x01] GOTO 0x0049
 12: 0x0039 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0049
 13: 0x0041 [0x03] Work_Zone[1] = 1073741824*
 14: 0x0046 [0x01] GOTO 0x0049

SUBROUTINE_0049:
 15: 0x0049 [0x1C] WAIT(30* ticks)
 16: 0x004C [0x21] END_EVENT
 17: 0x004D [0x00] END_REQSTACK()
```
