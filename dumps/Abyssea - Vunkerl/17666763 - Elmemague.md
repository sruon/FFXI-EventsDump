# 17666763 - Elmemague

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Vunkerl (ID: 217) |
| Block Size       | 128 bytes                   |
| Total Events     | 4                           |
| References Count | 7                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1080](#event-1080)   | 0x0001       |     15 |              7 |
| [1081](#event-1081)   | 0x0010       |     32 |             13 |
| [1082](#event-1082)   | 0x0030       |     20 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x20DE      |        8414 |
|       1 | 0x20DF      |        8415 |
|       2 | 0x20DC      |        8412 |
|       3 | 0x20DD      |        8413 |
|       4 | 0x0000      |           0 |
|       5 | 0x20E0      |        8416 |
|       6 | 0x20E1      |        8417 |

## String References

- **8412**: Right on time! You can just set that down right here.
- **8413**: Splendid! A more dependable courier I've never seen. You can go back and claim your reward from what's-his-name at the central base.
- **8414**: Is this your first time visiting the outpost, by any chance? This is our key stronghold--our bastion, as it were--in the battle to drive back the Abyssean hordes once and for all.
- **8415**: Needless to say, the resistance could always use another capable soldier like yourself. If you're willing to lend your strength to our cause, just speak with the resistance sapper over there.
- **8416**: Hm? Your mission was to deliver our supplies, not a load of rubbish. You didn't think you could get away with taking a shortcut through a conflux, did you?
- **8417**: I thought I'd seen the last of this when I removed that slacker from active duty. It pains me indeed to see that you were cut from the same laggard cloth.

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

### Event 1080

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8414*)
    → "Is this your first time visiting the outpost, by any chance? This is our key stronghold--our bastion, as it were--in the battle to drive back the Abyssean hordes once and for all."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8415*)
    → "Needless to say, the resistance could always use another capable soldier like yourself. If you're willing to lend your strength to our cause, just speak with the resistance sapper over there."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 1081

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 32 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 42 1E F0 FF FF 7F 1D 02  80 23 1D 03 80 23 02 02  B........#...#..
0020: 10 04 80 00 2E 00 1D 00  80 23 1D 01 80 23 21 00  .........#...#!.
```

#### Opcodes

```
  0: 0x0010 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=8412*)
    → "Right on time! You can just set that down right here."
  3: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=8413*)
    → "Splendid! A more dependable courier I've never seen. You can go back and claim your reward from what's-his-name at the central base."
  5: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001E [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x002E
  7: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=8414*)
    → "Is this your first time visiting the outpost, by any chance? This is our key stronghold--our bastion, as it were--in the battle to drive back the Abyssean hordes once and for all."
  8: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002A [0x1D] PRINT_EVENT_MESSAGE(message_id=8415*)
    → "Needless to say, the resistance could always use another capable soldier like yourself. If you're willing to lend your strength to our cause, just speak with the resistance sapper over there."
 10: 0x002D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x002E [0x21] END_EVENT
 12: 0x002F [0x00] END_REQSTACK()
```

### Event 1082

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 20 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 42 1E F0 FF FF 7F 1D 02  80 23 1D 05 80 23 1D 06  B........#...#..
0040: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0030 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0031 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=8412*)
    → "Right on time! You can just set that down right here."
  3: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x003A [0x1D] PRINT_EVENT_MESSAGE(message_id=8416*)
    → "Hm? Your mission was to deliver our supplies, not a load of rubbish. You didn't think you could get away with taking a shortcut through a conflux, did you?"
  5: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=8417*)
    → "I thought I'd seen the last of this when I removed that slacker from active duty. It pains me indeed to see that you were cut from the same laggard cloth."
  7: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0042 [0x21] END_EVENT
  9: 0x0043 [0x00] END_REQSTACK()
```
